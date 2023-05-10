import sys
from pygame import *
from BBkeybindings import *
from BBimg import *

wide = 1280
tall = 700
screen = pygame.display.set_mode((wide, tall))

# sprite groups
all22 = pygame.sprite.LayeredUpdates()
active = pygame.sprite.Group()
inactive = pygame.sprite.Group()
offense = pygame.sprite.Group()
receivers = pygame.sprite.Group()
defense = pygame.sprite.Group()

# other variables
running = True
play = False
clock = pygame.time.Clock()
snapped = 0
slid = 0
dove = 0
set = 0

#####################################
# Every yard line is 23 pixels and  #
# every 5 yards is 115 pixels total #
#####################################
middle = (wide/2)-18
line = 511
down = 0
kickoff = True
# positional variables
    # "active" player's coords
active_X = 0
active_Y = 0
    # "active" player's starting coords
static_X = 0
static_Y = 400
    # where the ball needs to be spotted
touchback_Y = -1456
spot_X = 0 # will be for positioning the center left and right
spot_Y = 0 # is for positioning the field up and down; -1456 is the spot for a touchback, will be changed later
    # location of the center
center_X = 0
center_Y = 0
    # size of the player images
half_X = 18
half_Y = 14


class ATHLETE(pygame.sprite.Sprite):
    def __init__(self):
        super(ATHLETE, self).__init__()
        self.auto_move = 8
        self.speed = 5

    def snap(self, auto_move):
        self.rect.move_ip(0, -auto_move/3)

    def slide(self, speed):
        self.rect.move_ip(0, speed/2)

    def ends(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, -5)

    def bounds(self, pressed_keys):
        if pressed_keys[left]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[right]:
            self.rect.move_ip(5, 0)


class OFFENSIVE_BACK(ATHLETE):
    def __init__(self):
        super(OFFENSIVE_BACK, self).__init__()
        self._layer = 14

    def shotgun(self):
        self.rect = self.surf.get_rect(
            topleft=(cnt.rect.x, cnt.rect.y+115)
        )

    def under(self):
        self.rect = self.surf.get_rect(
            topleft=(cnt.rect.x, cnt.rect.y+30)
        )


class QUARTERBACK(OFFENSIVE_BACK):
    def __init__(self):
        super(QUARTERBACK, self).__init__()
        self.surf = o4


class RUNNINGBACK(OFFENSIVE_BACK):
    def __init__(self):
        super(RUNNINGBACK, self).__init__()
        self.surf = o24

    def under(self):
        self.rect = self.surf.get_rect(
            topleft=(qb.rect.x+46, qb.rect.y+76)
        )
#(middle-46,shotgun+46),(middle+46,shotgun+46),(middle+46,shotgun-23),(middle-46,shotgun-23)


class RECEIVER(ATHLETE):
    def __init__(self):
        super(RECEIVER, self).__init__()
        self._layer = 12


class WIDERECEIVER(RECEIVER):
    def __init__(self):
        super(WIDERECEIVER, self).__init__()
        self.surf = o18

    def XL(self):
        self.rect = self.surf.get_rect(
            topleft=(60, cnt.rect.y)
        )

    def XR(self):
        self.rect = self.surf.get_rect(
            topleft=(1180, cnt.rect.y)
        )

    def slotL(self):
        self.rect = self.surf.get_rect(
            topleft=(160, cnt.rect.y+28)
        )


class TIGHT_END(RECEIVER):
    def __init__(self):
        super(TIGHT_END, self).__init__()
        self.surf = o86
        self.rect = self.surf.get_rect()

    def teR(self):
        self.rect = self.surf.get_rect(
            topleft=(cnt.rect.x+108, cnt.rect.y+7)
        )


class LINEMAN(ATHLETE):
    def __init__(self):
        super(LINEMAN, self).__init__()
        self._layer = 10
        self.surf = o57
        self.rect = self.surf.get_rect()

    def leftgaurd(self):
        self.rect = self.surf.get_rect(
            topleft=(cnt.rect.x-36,cnt.rect.y+7)
        )
        self.surf = o52

    def rightguard(self):
        self.rect = self.surf.get_rect(
            topleft=(cnt.rect.x+36, cnt.rect.y+7)
        )
        self.surf = o68

    def lefttackle(self):
        self.rect = self.surf.get_rect(
            topleft=(cnt.rect.x-72, cnt.rect.y+14)
        )
        self.surf = o71

    def righttackle(self):
        self.rect = self.surf.get_rect(
            topleft=(cnt.rect.x+72, cnt.rect.y+14)
        )
        self.surf = o62


class FIELD(ATHLETE):
    def __init__(self):
        super(FIELD, self).__init__()
        self.surf = area
        self._layer = 5
        self.rect = self.surf.get_rect()

    def spot(self):
        self.rect = self.surf.get_rect(
            topleft=(0,spot_Y)
        )

    def snap(self, auto_move):
        self.rect.move_ip(0, -auto_move/3)


class BALL(ATHLETE):
    def __init__(self):
        super(BALL, self).__init__()
        self.speed = -4
        self.surf = pigskin
        self._layer = 6

    def spot(self):
        self.rect = self.surf.get_rect(
            center=(cnt.rect.x+18,cnt.rect.y)
        )


fb = BALL()
field = FIELD()
qb = QUARTERBACK()
cnt = LINEMAN()
rg = LINEMAN()
lg = LINEMAN()
rt = LINEMAN()
lt = LINEMAN()
rb1 = RUNNINGBACK()
rb2 = RUNNINGBACK()
wr1 = WIDERECEIVER()
wr2 = WIDERECEIVER()
wr3 = WIDERECEIVER()
wr4 = WIDERECEIVER()
wr5 = WIDERECEIVER()
te1 = TIGHT_END()
te2 = TIGHT_END()
te3 = TIGHT_END()

pygame.init()

while running: # main game loop
    keystroke = pygame.key.get_pressed()
    if play is True: # prevents movement before the snap (does not prevent events, i.e snapping from moving sprites)
        for entity in inactive:
            entity.ends(keystroke)
        for entity in active:
            entity.bounds(keystroke)

    # draws the screen here
    for entity in all22:
        screen.blit(entity.surf, entity.rect)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit()
            if event.key == snap:
                if snapped == 0:
                    play = True
                    snapped = 1
                    down += 1
                    static_Y = field.rect.y # records the Y position of the QB at the snap (on keypress)
                    kickoff = False
            if event.key == slide:
                if slid == 0:
                    slid = 1
                    static_Y = field.rect.y
                    spot_Y = field.rect.y-36
                    if qb.rect.x > 693:
                        spot_X = 693
                    if qb.rect.x < 550:
                        spot_X = 550
                    if 550 < qb.rect.x < 693:
                        spot_X = qb.rect.x
            if event.key == clear:
                field.kill()
                for entity in all22:
                    entity.kill()
            if event.key == place: #for the groups below they will need to be moved later to the plays instead of here
                if kickoff == False:
                    field.rect.y = spot_Y
                    cnt.rect.x = spot_X
                    cnt.rect.y = line
                if kickoff == True:
                    field.rect.y = -1456
                    cnt.rect.x = middle
                    cnt.rect.y = line
                qb.under()
                fb.spot()
                rb1.under()
                wr1.XL()
                wr2.XR()
                wr3.slotL()
                te1.teR()
                lg.leftgaurd()
                lt.lefttackle()
                rg.rightguard()
                rt.righttackle()
                offense.add(
                    cnt, rb1, rg, lg, rt, lt, wr1, wr2, wr3, te1
                    #, receivers
                )
                inactive.add(
                    offense, field, fb
                )
                active.add(
                    qb
                )
                all22.add(
                    active, inactive
                )

        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    for entity in all22:
# snapping the ball is handled below this line (except events)
        if snapped == 1: # along with keypress above if the ball isn't snapped sets the variable to allow snapping
            fb.snap(fb.speed)
            if pygame.sprite.spritecollideany(fb, active):
                snapped = 2 # sets the ball so it can't be snapped in the middle of play
                fb.kill()
                slid = 0
        if snapped == 2:
            field.snap(field.auto_move)
            for entity in offense:
                entity.snap(entity.auto_move)
            for entity in defense:
                entity.snap(entity.auto_move)
            if field.rect.y <= static_Y-69:
                snapped = 3
            elif field.rect.y <= static_Y-138:
                snapped = 3
# sliding with the ball is handled below this line (except events)
        if snapped == 3: # allows a slide to occur only if the ball is snapped (and caught: TBD)
            if slid == 1:
                for entity in inactive:
                    entity.slide(entity.speed)
                if pygame.sprite.spritecollideany(qb, offense): # stops the slide (changing slid to 2) if collision occurs
                    slid = 2
                    play = False
                    snapped = 0
                    slid = 0
                    dove = 0
                    set = 0
                elif static_Y <= field.rect.y-92: # moving up the screen decreases the Y value, top left is (0,0)
                    slid = 2
                    play = False
                    snapped = 0
                    slid = 0
                    dove = 0
                    set = 0

    pygame.display.update()
    clock.tick(30)

