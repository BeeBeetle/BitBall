import pygame

# a list of all images used in the game and variables so it's easier to write

# base
pigskin = pygame.image.load("images/pigskin.png")
area = pygame.image.load("images/portrait.png")

#Offense
o1 = pygame.image.load("images/offense/1.png")
o2 = pygame.image.load("images/offense/2.png")
o3 = pygame.image.load("images/offense/3.png")
o4 = pygame.image.load("images/offense/4.png")
o5 = pygame.image.load("images/offense/5.png")
o6 = pygame.image.load("images/offense/6.png")
o7 = pygame.image.load("images/offense/7.png")
o8 = pygame.image.load("images/offense/8.png")
o9 = pygame.image.load("images/offense/9.png")
o10 = pygame.image.load("images/offense/10.png")
o11 = pygame.image.load("images/offense/11.png")
o12 = pygame.image.load("images/offense/12.png")
o13 = pygame.image.load("images/offense/13.png")
o14 = pygame.image.load("images/offense/14.png")
o15 = pygame.image.load("images/offense/15.png")
o16 = pygame.image.load("images/offense/16.png")
o17 = pygame.image.load("images/offense/17.png")
o18 = pygame.image.load("images/offense/18.png")
o19 = pygame.image.load("images/offense/19.png")
o20 = pygame.image.load("images/offense/20.png")
o21 = pygame.image.load("images/offense/21.png")
o22 = pygame.image.load("images/offense/22.png")
o23 = pygame.image.load("images/offense/23.png")
o24 = pygame.image.load("images/offense/24.png")
o25 = pygame.image.load("images/offense/25.png")
o26 = pygame.image.load("images/offense/26.png")
o27 = pygame.image.load("images/offense/27.png")
o28 = pygame.image.load("images/offense/28.png")
o29 = pygame.image.load("images/offense/29.png")
o30 = pygame.image.load("images/offense/30.png")
o31 = pygame.image.load("images/offense/31.png")
o32 = pygame.image.load("images/offense/32.png")
o33 = pygame.image.load("images/offense/33.png")
o34 = pygame.image.load("images/offense/34.png")
o35 = pygame.image.load("images/offense/35.png")
o36 = pygame.image.load("images/offense/36.png")
o37 = pygame.image.load("images/offense/37.png")
o38 = pygame.image.load("images/offense/38.png")
o39 = pygame.image.load("images/offense/39.png")
o40 = pygame.image.load("images/offense/40.png")
o41 = pygame.image.load("images/offense/41.png")
o42 = pygame.image.load("images/offense/42.png")
o43 = pygame.image.load("images/offense/43.png")
o44 = pygame.image.load("images/offense/44.png")
o45 = pygame.image.load("images/offense/45.png")
o46 = pygame.image.load("images/offense/46.png")
o47 = pygame.image.load("images/offense/47.png")
o48 = pygame.image.load("images/offense/48.png")
o49 = pygame.image.load("images/offense/49.png")
o50 = pygame.image.load("images/offense/50.png")
o51 = pygame.image.load("images/offense/51.png")
o52 = pygame.image.load("images/offense/52.png")
o53 = pygame.image.load("images/offense/53.png")
o54 = pygame.image.load("images/offense/54.png")
o55 = pygame.image.load("images/offense/55.png")
o56 = pygame.image.load("images/offense/56.png")
o57 = pygame.image.load("images/offense/57.png")
o58 = pygame.image.load("images/offense/58.png")
o59 = pygame.image.load("images/offense/59.png")
o60 = pygame.image.load("images/offense/60.png")
o61 = pygame.image.load("images/offense/61.png")
o62 = pygame.image.load("images/offense/62.png")
o63 = pygame.image.load("images/offense/63.png")
o64 = pygame.image.load("images/offense/64.png")
o65 = pygame.image.load("images/offense/65.png")
o66 = pygame.image.load("images/offense/66.png")
o67 = pygame.image.load("images/offense/67.png")
o68 = pygame.image.load("images/offense/68.png")
o69 = pygame.image.load("images/offense/69.png")
o70 = pygame.image.load("images/offense/70.png")
o71 = pygame.image.load("images/offense/71.png")
o72 = pygame.image.load("images/offense/72.png")
o73 = pygame.image.load("images/offense/73.png")
o74 = pygame.image.load("images/offense/74.png")
o75 = pygame.image.load("images/offense/75.png")
o76 = pygame.image.load("images/offense/76.png")
o77 = pygame.image.load("images/offense/77.png")
o78 = pygame.image.load("images/offense/78.png")
o79 = pygame.image.load("images/offense/79.png")
o80 = pygame.image.load("images/offense/80.png")
o81 = pygame.image.load("images/offense/81.png")
o82 = pygame.image.load("images/offense/82.png")
o83 = pygame.image.load("images/offense/83.png")
o84 = pygame.image.load("images/offense/84.png")
o85 = pygame.image.load("images/offense/85.png")
o86 = pygame.image.load("images/offense/86.png")
o87 = pygame.image.load("images/offense/87.png")
o88 = pygame.image.load("images/offense/88.png")
o89 = pygame.image.load("images/offense/89.png")
o90 = pygame.image.load("images/offense/90.png")
o91 = pygame.image.load("images/offense/91.png")
o92 = pygame.image.load("images/offense/92.png")
o93 = pygame.image.load("images/offense/93.png")
o94 = pygame.image.load("images/offense/94.png")
o95 = pygame.image.load("images/offense/95.png")
o96 = pygame.image.load("images/offense/96.png")
o97 = pygame.image.load("images/offense/97.png")
o98 = pygame.image.load("images/offense/98.png")
o99 = pygame.image.load("images/offense/99.png")
#Defense
d1 = pygame.image.load("images/defense/1.png")
d2 = pygame.image.load("images/defense/2.png")
d3 = pygame.image.load("images/defense/3.png")
d4 = pygame.image.load("images/defense/4.png")
d5 = pygame.image.load("images/defense/5.png")
d6 = pygame.image.load("images/defense/6.png")
d7 = pygame.image.load("images/defense/7.png")
d8 = pygame.image.load("images/defense/8.png")
d9 = pygame.image.load("images/defense/9.png")
d10 = pygame.image.load("images/defense/10.png")
d11 = pygame.image.load("images/defense/11.png")
d12 = pygame.image.load("images/defense/12.png")
d13 = pygame.image.load("images/defense/13.png")
d14 = pygame.image.load("images/defense/14.png")
d15 = pygame.image.load("images/defense/15.png")
d16 = pygame.image.load("images/defense/16.png")
d17 = pygame.image.load("images/defense/17.png")
d18 = pygame.image.load("images/defense/18.png")
d19 = pygame.image.load("images/defense/19.png")
d20 = pygame.image.load("images/defense/20.png")
d21 = pygame.image.load("images/defense/21.png")
d22 = pygame.image.load("images/defense/22.png")
d23 = pygame.image.load("images/defense/23.png")
d24 = pygame.image.load("images/defense/24.png")
d25 = pygame.image.load("images/defense/25.png")
d26 = pygame.image.load("images/defense/26.png")
d27 = pygame.image.load("images/defense/27.png")
d28 = pygame.image.load("images/defense/28.png")
d29 = pygame.image.load("images/defense/29.png")
d30 = pygame.image.load("images/defense/30.png")
d31 = pygame.image.load("images/defense/31.png")
d32 = pygame.image.load("images/defense/32.png")
d33 = pygame.image.load("images/defense/33.png")
d34 = pygame.image.load("images/defense/34.png")
d35 = pygame.image.load("images/defense/35.png")
d36 = pygame.image.load("images/defense/36.png")
d37 = pygame.image.load("images/defense/37.png")
d38 = pygame.image.load("images/defense/38.png")
d39 = pygame.image.load("images/defense/39.png")
d40 = pygame.image.load("images/defense/40.png")
d41 = pygame.image.load("images/defense/41.png")
d42 = pygame.image.load("images/defense/42.png")
d43 = pygame.image.load("images/defense/43.png")
d44 = pygame.image.load("images/defense/44.png")
d45 = pygame.image.load("images/defense/45.png")
d46 = pygame.image.load("images/defense/46.png")
d47 = pygame.image.load("images/defense/47.png")
d48 = pygame.image.load("images/defense/48.png")
d49 = pygame.image.load("images/defense/49.png")
d50 = pygame.image.load("images/defense/50.png")
d51 = pygame.image.load("images/defense/51.png")
d52 = pygame.image.load("images/defense/52.png")
d53 = pygame.image.load("images/defense/53.png")
d54 = pygame.image.load("images/defense/54.png")
d55 = pygame.image.load("images/defense/55.png")
d56 = pygame.image.load("images/defense/56.png")
d57 = pygame.image.load("images/defense/57.png")
d58 = pygame.image.load("images/defense/58.png")
d59 = pygame.image.load("images/defense/59.png")
d60 = pygame.image.load("images/defense/60.png")
d61 = pygame.image.load("images/defense/61.png")
d62 = pygame.image.load("images/defense/62.png")
d63 = pygame.image.load("images/defense/63.png")
d64 = pygame.image.load("images/defense/64.png")
d65 = pygame.image.load("images/defense/65.png")
d66 = pygame.image.load("images/defense/66.png")
d67 = pygame.image.load("images/defense/67.png")
d68 = pygame.image.load("images/defense/68.png")
d69 = pygame.image.load("images/defense/69.png")
d70 = pygame.image.load("images/defense/70.png")
d71 = pygame.image.load("images/defense/71.png")
d72 = pygame.image.load("images/defense/72.png")
d73 = pygame.image.load("images/defense/73.png")
d74 = pygame.image.load("images/defense/74.png")
d75 = pygame.image.load("images/defense/75.png")
d76 = pygame.image.load("images/defense/76.png")
d77 = pygame.image.load("images/defense/77.png")
d78 = pygame.image.load("images/defense/78.png")
d79 = pygame.image.load("images/defense/79.png")
d80 = pygame.image.load("images/defense/80.png")
d81 = pygame.image.load("images/defense/81.png")
d82 = pygame.image.load("images/defense/82.png")
d83 = pygame.image.load("images/defense/83.png")
d84 = pygame.image.load("images/defense/84.png")
d85 = pygame.image.load("images/defense/85.png")
d86 = pygame.image.load("images/defense/86.png")
d87 = pygame.image.load("images/defense/87.png")
d88 = pygame.image.load("images/defense/88.png")
d89 = pygame.image.load("images/defense/89.png")
d90 = pygame.image.load("images/defense/90.png")
d91 = pygame.image.load("images/defense/91.png")
d92 = pygame.image.load("images/defense/92.png")
d93 = pygame.image.load("images/defense/93.png")
d94 = pygame.image.load("images/defense/94.png")
d95 = pygame.image.load("images/defense/95.png")
d96 = pygame.image.load("images/defense/96.png")
d97 = pygame.image.load("images/defense/97.png")
d98 = pygame.image.load("images/defense/98.png")
d99 = pygame.image.load("images/defense/99.png")

