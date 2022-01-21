import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
import pyperclip

ench__ = "" # placeholder nbt
ench__2 = ""

root = Tk() # basic app
root.title("NBT Builder")
root.configure(bg='black')

font = Font(family="Uni Sans Heavy") # font


 # tabs
kitmaker = ttk.Notebook(root)
kitmaker.grid(row=0, column=0)

frame_tabkit = Frame(kitmaker, bg="black")
frame_tabsingle = Frame(kitmaker, bg="black")

frame_tabkit.grid(row=0, column=0)
frame_tabsingle.grid(row=0, column=1)

kitmaker.add(frame_tabsingle, text="single")
kitmaker.add(frame_tabkit, text="Kit Maker")



frame = LabelFrame(frame_tabsingle, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
frame.grid(row=1, column=1, columnspan=2)


def name(): # put in name
    global ench__

    nbt1 = '{Count:' + str(amount.get()) + 'b,Damage:14s,Name:"minecraft:' + str(itemname.get()) + '",Slot:14b,WasPickedUp:0b,tag:{ench:['

    nbtbox.config(state = "normal")
    nbtbox.insert(END , nbt1)
    nbtbox.config(state="disabled")

    ench__ += nbt1

def ench():
    global ench__

    nbt2 = '{id:' + str(enchantid.get()) + 's,lvl:' + str(lvl.get()) + 's},'

    nbtbox.config(state="normal")
    nbtbox.insert(END, nbt2)
    nbtbox.config(state="disabled")

    ench__ += nbt2

def finish():
    global ench__

    ench__ += ']}}],RepairCost:0,display:{Name:"Caplini"}}>,RepairCost:0,display:{Name:"Caplini"}}'

    nbtbox.config(state="normal")
    nbtbox.insert(END, ench__)
    nbtbox.config(state="disabled")

    pyperclip.copy(ench__)

    #nbtbox.tag_configure('right', justify='right')

def clear():
    nbtbox.config(state="normal")
    nbtbox.delete(1.0, END)
    nbtbox.config(state="disabled")

    itemname.delete(0, END)
    amount.delete(0, END)
    enchantid.delete(0, END)
    lvl.delete(0, END)

    global ench__
    ench__ = ""

def IDS(): # id button command
    root = Tk()
    root.title("ID's")
    root.configure(bg='black')

    IDS = Text(root, width=36, height=20, borderwidth=1, fg="green", bg="black", font=font)
    IDS.grid(row=0, column=0, padx=5, pady=7)
    IDS.config(state="normal")
    IDS.insert(1.0, "protection - 0\n\nfire_protection - 1\n\nfeather_falling - 2\n\nblast_protection - 3\n\nprojectile_protection - 4\n\nthorns - 5\n\nrespiration - 6\n\ndepth_strider - 7\n\naqua_affinity - 8\n\nsharpness - 9\n\nsmite - 10\n\nbane_of_arthropods - 11\n\nknockback - 12\n\nfire_aspect - 13\n\nlooting - 14\n\nefficiency - 15\n\nsilck_touch - 16\n\nunbreaking - 17\n\nfortune - 18\n\npower - 19\n\npunch - 20\n\nflame - 21\n\ninfinity - 22\n\nluck_of_the_sea - 23\n\nlure - 24\n\nfrost_walker - 25\n\nmending - 26\n\nbinding_curse - 27\n\nvanishing_curse - 28")
    IDS.config(state="disabled")

    ITEM = Text(root, width=36, height=20, borderwidth=1, fg="green", bg="black", font=font)
    ITEM.grid(row=0, column=1, padx=5, pady=7)
    ITEM.config(state="normal")
    ITEM.insert(1.0, "air\n\nstone\n\ngrass\n\ndirt\n\ncobblestone\n\nplanks\n\nsapling\n\nbedrock\n\nflowing_water\n\nwater\n\nflowing_lava\n\nlava\n\nsand\n\ngravel\n\ngold_ore\n\niron_ore\n\ncoal_ore\n\nlog\n\nleaves\n\nsponge\n\nglass\n\nlapis_ore\n\nlapis_block\n\ndispenser\n\nsandstone\n\nnoteblock\n\nbed\n\ngolden_rail\n\ndetector_rail\n\nsticky_piston\n\nweb\n\ntallgrass\n\npiston\n\npiston_head\n\nwool\n\nyellow_flower\n\nred_flower\n\nbrown_mushroom\n\nred_mushroom\n\ngold_block\n\niron_block\n\ndouble_stone_slab\n\nstone_slab\n\ntnt\n\nbookshelf\n\nmossy_cobblestone\n\nobsidian\n\ntorch\n\nfire\n\nmob_spawner\n\noak_stairs\n\nchest\n\nredstone_wire\n\ndiamond_ore\n\ndiamond_block\n\ncrafting_table\n\nwheat\n\nfarmland\n\nfurnace\n\nlit_furnace\n\nstanding_sign\n\nwooden_door\n\nladder\n\nrail\n\nstone_stairs\n\nwall_sign\n\nlever\n\nstone_preassure_plate\n\niron_door\n\nwooden_pressure_plate\n\nredstone_ore\n\nlit_redstone_ore\n\nunlit_restone_torch\n\nredstone_torch\n\nstone_button\n\nsnow_layer\n\nice\n\nsnow\n\ncactus\n\nclay\n\nreeds\n\njukebox\n\nfence\n\npumkin\n\nnetherrack\n\nsoul_sand\n\nglowstone\n\nportal\n\nlit_pumkin\n\ncake\n\nunpowerd_repeater\n\npowerd_repeater\n\nstained_glass\n\nmonster_egg\n\nstonebrick\n\nbrown_mushroom_block\n\nred_mushroom_block\n\niron_bars\n\nglass_pane\n\nmelon_block\n\npumkin_stem\n\nnmelon_stem\n\nvine\n\nfence_gate\n\nbrick_stairs\n\nstone_brick_stairs\n\nmycelium\n\nwaterlily\n\nnether_brick\n\nnether_brick_fence\n\nnether_brick_stairs\n\nnether_wart\n\nenchanting_table\n\nbrewing_stand\n\ncauldron\n\nend_portal\n\nend_portal_frame\n\nend_stone\n\ndragon_egg\n\nredstone_lamp\n\nlit_redstone_lamp\n\ndouble_wooden_slab\n\nwooden_slab\n\ncoca\n\nsandstone_stairs\n\nemerald_ore\n\nender_chest\n\ntripwire_hook\n\nemerald_block\n\nspruce_stairs\n\nbirch_stairs\n\njungle_stairs\n\ncomman_block\n\nbeacon\n\ncobblestone_wall\n\nflower_pot\n\ncarrots\n\npotatoes\n\nwooden_button\n\nskull\n\nanvil\n\ntrapped_chest\n\nlight_weighted_pressure_plate\n\nheavy_weighted_pressure_plate\n\nunpowered_comparator\n\npowered_comparator\n\ndaylight_detector\n\nredstone_block\n\nquartz_ore\n\nhopper\n\nquartz_block\n\nquartz_stairs\n\nactivator_rail\n\ndropper\n\nstained_hardened_clay\n\nstained_glass_pane\n\nleaves2\n\nlog2\n\nacacia_stairs\n\ndark_oak\n\nstairs\n\nslime\n\nbarrier\n\niron_trapdoor\n\nprismarine\n\nsea_lantern\n\nhay_block\n\ncarpet\n\nhardened_clay\n\ncoal_block\n\npacked_ice\n\ndouble_plant\n\nstanding_banner\n\nwall_banner\n\ndaylight_detector_inverted\n\nred_sandstone\n\nred_sandstone_stairs\n\ndouble_stone_slab2\n\nstone_slab2\n\nspruce_fence_gate\n\nbirch_fence_gate\n\njungle_fence_gate\n\ndark_oak_fence_gate\n\nacacia_fence_gate\n\nspruce_fence\n\nbirch_fence\n\njungle_fence\n\ndark_oak_fence\n\nacacia_fence\n\nspruce_door\n\nbirch_door\n\njungle_door\n\nacacia_door\n\ndark_oak_door\n\nend_rod\n\nchorus_plant\n\nchorus_flower\n\npurpur_block\n\npurpur_pillar\n\npurpur_stairs\n\npurpur_double_slab\n\npurpur_slab\n\nend_bricks\n\nbeetroots\n\ngrass_path\n\nend_gateway\n\nrepeating_command_block\n\nchain_command_block\n\nfrosted_ice\n\nnether_wart_block\n\nred_nether_brick\n\nbone_block\n\nstructure_void\n\nobserver\n\nwhite_shulker_box\n\norange_shulker_box\n\nmagenta_shulker_box\n\nlight_blue_shulker_box\n\nyellow_shulker_box\n\nlime_shulker_box\n\npink_shulker_box\n\ngray_shulker_box\n\nsilver_shulker_box\n\ncyan_shulker_box\n\npurple_shulker_box\n\nblue_shulker_box\n\nbrown_shulker_box\n\ngreen_shulker_box\n\nred_shulker_box\n\nblack_shulker_box\n\nwhite_glazed_terracotta\n\norange_glazed_terracotta\n\nmagenta_glazed_terracotta\n\nlight_blue_glazed_terracotta\n\nyellow_glazed_terracotta\n\nlime_glazed_terracotta\n\npink_glazed_terracotta\n\ngray_glazed_terracotta\n\nlight_gray_glazed_terracotta\n\ncyan_glazed_terracotta\n\npurple_glazed_terracotta\n\nblue_glazed_terracotta\n\nbrown_glazed_terracotta\n\ngreen_glazed_terracotta\n\nred_glazed_terracotta\n\nblack_glazed_terracotta\n\nconcrete\n\nconcrete_powder\n\nstructure_block\n\niron_shovel\n\niron_pickaxe\n\niron_axe\n\nflint_and_steel\n\napple\n\nbow\n\narrow\n\ncoal\n\ncoal\n\ndiamond\n\niron_ingot\n\ngold_ingot\n\niron_sword\n\nwooden_sword\n\nwooden_shovel\n\nwooden_pickaxe\n\nwooden_axe\n\nstone_sword\n\nstone_shovel\n\nstone_pickaxe\n\nstone_axe\n\ndiamond_sword\n\ndiamond_shovel\n\ndiamond_pickaxe\n\ndiamond_axe\n\nstick\n\nbowl\n\nmushroom_stew\n\ngolden_sword\n\ngolden_shovel\n\ngolden_pickaxe\n\ngolden_axe\n\nstring\n\nfeather\n\ngunpowder\n\nwooden_hoe\n\nstone_hoe\n\niron_hoe\n\ndiamond_hoe\n\ngolden_hoe\n\nwheat_seeds\n\nwheat\n\nbread\n\nleather_helmet\n\nleather_chestplate\n\nleather_leggings\n\nleather_boots\n\nchainmail_helmet\n\nchainmail_chestplate\n\nchainmail_leggings\n\nchainmail_boots\n\niron_helmet\n\niron_chestplate\n\niron_leggings\n\niron_boots\n\ndiamond_helmet\n\ndiamond_chestplate\n\ndiamond_leggings\n\ndiamond_boots\n\ngolden_helmet\n\ngolden_chestplate\n\ngolden_leggings\n\ngolden_boots\n\nflint\n\nporkchop\n\ncooked_porkchop\n\npainting\n\ngolden_apple\n\ngolden_apple\n\nsign\n\nwooden_door\n\nbucket\n\nwater_bucket\n\nlava_bucket\n\nminecart\n\nsaddle\n\niron_door\n\nredstone\n\nsnowball\n\nboat\n\nleather\n\nmilk_bucket\n\nbrick\n\nclay_ball\n\nreeds\n\npaper\n\nbook\n\nslime_ball\n\nchest_minecart\n\nfurnace_minecart\n\negg\n\ncompass\n\nfishing_rod\n\nclock\n\nglowstone_dust\n\nfish\n\ncooked_fish\n\ndye\n\ncake\n\nbed\n\n \n\nrepeater\n\ncookie\n\nfilled_map\n\nshears\n\nmelon\n\npumpkin_seeds\n\nmelon_seeds\n\nbeef\n\ncooked_beef\n\nchicken\n\ncooked_chicken\n\nrotten_flesh\n\nender_pearl\n\nblaze_rod\n\nghast_tear\n\ngold_nugget\n\nnether_wart\n\npotion\n\nglass_bottle\n\nspider_eye\n\nfermented_spider_eye\n\nblaze_powder\n\nmagma_cream\n\nbrewing_stand\n\ncauldron\n\nender_eye\n\nspeckled_melon\n\nspawn_egg\n\nexperience_bottle\n\nfire_charge\n\nwritable_book\n\nwritten_book\n\nemerald\n\nitem_frame\n\nflower_pot\n\ncarrot\n\npotato\n\nbaked_potato\n\npoisonous_potato\n\nmap\n\ngolden_carrot\n\ncarrot_on_a_stick\n\nnether_star\n\npumpkin_pie\n\nfireworks\n\nfirework_charge\n\nenchanted_book\n\ncomparator\n\nnetherbrick\n\nquartz\n\ntnt_minecart\n\nhopper_minecart\n\nprismarine_shard\n\nprismarine_crystals\n\nrabbit\n\ncooked_rabbit\n\nrabbit_stew\n\nrabbit_foot\n\nrabbit_hide\n\narmor_stand\n\niron_horse_armor\n\ngolden_horse_armor\n\ndiamond_horse_armor\n\nlead\n\nname_tag\n\ncommand_block_minecart\n\nmutton\n\ncooked_mutton\n\nbanner\n\nend_crystal\n\nspruce_door\n\nbirch_door\n\njungle_door\n\nacacia_door\n\ndark_oak_door\n\nchorus_fruit\n\npopped_chorus_fruit\n\nbeetroot\n\nbeetroot_seeds\n\nbeetroot_soup\n\ndragon_breath\n\nsplash_potion\n\nspectral_arrow\n\ntipped_arrow\n\nlingering_potion\n\nshield\n\nelytra\n\nspruce_boat\n\nbirch_boat\n\njungle_boat\n\nacacia_boat\n\ndark_oak_boat\n\ntotem_of_undying\n\nshulker_shell\n\niron_nugget\n\nknowledge_book\n\nrecord_13\n\nrecord_cat\n\nrecord_blocks\n\nrecord_chirp\n\nrecord_far\n\nrecord_mall\n\nrecord_mellohi\n\nrecord_stal\n\nrecord_strad\n\nrecord_ward\n\nrecord_11\n\nrecord_wait")
    ITEM.config(state="disabled")

    root.mainloop()


 # {Count:1b,Damage:53s,Name:"minecraft:shulker_box",Slot:1b,WasPickedUp:0b,tag:{Items:[{Count:2b,Damage:0s,Name:"minecraft:bow",Slot:0b,WasPickedUp:0b,tag:{ench:[{id:9s,lvl:32676s}]}}],RepairCost:0,display:{Name:"caplini",Lore:["Caplini"]}}}

# main box
nbtbox = Text(frame_tabsingle, width=36, height=20, borderwidth=1, fg="green", bg="black", font=font)
nbtbox.grid(row=1, column=0, padx=5, pady=7)
nbtbox.insert(1.0, ench__)
nbtbox.config(state = "disabled")

# item chose
itemname = Entry(frame, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
itemname.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
itemname.insert(0, "Item Name & Amount")

# item amount
amount = Entry(frame, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
amount.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

# enter item into nbt
enter = Button(frame, height=1, text="Enter", bg="black", fg="green", command=name)
enter.grid(row=0, column=3, padx=3, pady=3, rowspan=1)


# enter enchants
enchantid = Entry(frame, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
enchantid.grid(row=1, column=1, padx=3, pady=3,)
enchantid.insert(0, "Enchant ID & Level")

# enter enchant lvl
lvl = Entry(frame, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
lvl.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

# enter ench into nbt
enchenter = Button(frame, height=1, text="Enter", bg="black", fg="green", command=ench)
enchenter.grid(row=1, column=3, padx=3, pady=3, rowspan=1)


# finish
finish = Button(frame_tabsingle, height=1, width=18, text="Finish", font=("Uni Sans Heavy", 23), bg="black", fg="green", command=finish)
finish.grid(row=2, column=0, padx=3, pady=1)


# clear
clear = Button(frame, height=1, width=30, text="Clear", font=("Uni Sans Heavy", 14), bg="black", fg="green", comman=clear)
clear.grid(row=2, column=1, columnspan=3, padx=3, pady=1, sticky="W")


# id lists
id = Button(frame_tabsingle, height=1, width=3, text="ID's", font=("Uni Sans Heavy", 15), bg="black", fg="green", command=IDS)
id.grid(row=1, column=2, padx=3, pady=1, sticky="s, e")



####################################

amount1_ = ""
itemname1_ = ""

enchantid1_ = ""
lvl1_ = ""

enchant = ""



def box1():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r1button1.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname1_
        global amount1_

        itemname1_ += str(itemname1.get())
        itemname1_ = itemname1_

        amount1_ += str(amount1.get())
        amount1_ = amount1_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname1_ = ""
        itemname1.delete(0, END)
        amount1_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant

        enchant += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'

    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)


amount2_ = ""
itemname2_ = ""

enchantid2_ = ""
lvl2_ = ""

enchant2 = ""

def box2():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r1button2.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname2_
        global amount2_

        itemname2_ += str(itemname1.get())
        itemname2_ = itemname2_

        amount2_ += str(amount1.get())
        amount2_ = amount2_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname2_ = ""
        itemname1.delete(0, END)
        amount2_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global lvl2_
        global enchant2

        enchant2 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'

    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)


amount3_ = ""
itemname3_ = ""

enchantid3_ = ""
lvl3_ = ""

enchant3 = ""



def box3():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r1button3.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname3_
        global amount3_

        itemname3_ += str(itemname1.get())
        itemname3_ = itemname3_

        amount3_ += str(amount1.get())
        amount3_ = amount3_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname3_ = ""
        itemname1.delete(0, END)
        amount3_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant3

        enchant3 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount4_ = ""
itemname4_ = ""

enchantid4_ = ""
lvl4_ = ""

enchant4 = ""



def box4():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r1button4.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname4_
        global amount4_

        itemname4_ += str(itemname1.get())
        itemname4_ = itemname4_

        amount4_ += str(amount1.get())
        amount4_ = amount4_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname4_ = ""
        itemname1.delete(0, END)
        amount4_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant4

        enchant4 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount5_ = ""
itemname5_ = ""

enchantid5_ = ""
lvl5_ = ""

enchant5 = ""



def box5():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r1button5.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname5_
        global amount5_

        itemname5_ += str(itemname1.get())
        itemname5_ = itemname5_

        amount5_ += str(amount1.get())
        amount5_ = amount5_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname5_ = ""
        itemname1.delete(0, END)
        amount5_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant5

        enchant5 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount6_ = ""
itemname6_ = ""

enchantid6_ = ""
lvl6_ = ""

enchant6 = ""



def box6():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r1button6.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname6_
        global amount6_

        itemname6_ += str(itemname1.get())
        itemname6_ = itemname6_

        amount6_ += str(amount1.get())
        amount6_ = amount6_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname6_ = ""
        itemname1.delete(0, END)
        amount6_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant6

        enchant6 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount7_ = ""
itemname7_ = ""

enchantid7_ = ""
lvl7_ = ""

enchant7 = ""



def box7():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r1button7.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname7_
        global amount7_

        itemname7_ += str(itemname1.get())
        itemname7_ = itemname7_

        amount7_ += str(amount1.get())
        amount7_ = amount7_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname7_ = ""
        itemname1.delete(0, END)
        amount7_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant7

        enchant7 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount8_ = ""
itemname8_ = ""

enchantid8_ = ""
lvl8_ = ""

enchant8 = ""



def box8():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r1button8.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname8_
        global amount8_

        itemname8_ += str(itemname1.get())
        itemname8_ = itemname8_

        amount8_ += str(amount1.get())
        amount8_ = amount8_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname8_ = ""
        itemname1.delete(0, END)
        amount8_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant8

        enchant8 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount9_ = ""
itemname9_ = ""

enchantid9_ = ""
lvl9_ = ""

enchant9 = ""



def box9():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r1button9.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname9_
        global amount9_

        itemname9_ += str(itemname1.get())
        itemname9_ = itemname9_

        amount9_ += str(amount1.get())
        amount9_ = amount9_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname9_ = ""
        itemname1.delete(0, END)
        amount9_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant9

        enchant9 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount10_ = ""
itemname10_ = ""

enchantid10_ = ""
lvl10_ = ""

enchant10 = ""



def box10():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r2button1.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname10_
        global amount10_

        itemname10_ += str(itemname1.get())
        itemname10_ = itemname10_

        amount10_ += str(amount1.get())
        amount10_ = amount10_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname10_ = ""
        itemname1.delete(0, END)
        amount10_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant10

        enchant10 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount11_ = ""
itemname11_ = ""

enchantid11_ = ""
lvl11_ = ""

enchant11 = ""



def box11():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r2button2.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname11_
        global amount11_

        itemname11_ += str(itemname1.get())
        itemname11_ = itemname11_

        amount11_ += str(amount1.get())
        amount11_ = amount11_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname11_ = ""
        itemname1.delete(0, END)
        amount11_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant11

        enchant11 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount12_ = ""
itemname12_ = ""

enchantid12_ = ""
lvl12_ = ""

enchant12 = ""



def box12():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r2button3.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname12_
        global amount12_

        itemname12_ += str(itemname1.get())
        itemname12_ = itemname12_

        amount12_ += str(amount1.get())
        amount12_ = amount12_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname12_ = ""
        itemname1.delete(0, END)
        amount12_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant12

        enchant12 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount13_ = ""
itemname13_ = ""

enchantid13_ = ""
lvl13_ = ""

enchant13 = ""



def box13():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r2button4.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname13_
        global amount13_

        itemname13_ += str(itemname1.get())
        itemname13_ = itemname13_

        amount13_ += str(amount1.get())
        amount13_ = amount13_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname13_ = ""
        itemname1.delete(0, END)
        amount13_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant13

        enchant13 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount14_ = ""
itemname14_ = ""

enchantid14_ = ""
lvl14_ = ""

enchant14 = ""



def box14():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r2button5.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname14_
        global amount14_

        itemname14_ += str(itemname1.get())
        itemname14_ = itemname14_

        amount14_ += str(amount1.get())
        amount14_ = amount14_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname14_ = ""
        itemname1.delete(0, END)
        amount14_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant14

        enchant14 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount15_ = ""
itemname15_ = ""

enchantid15_ = ""
lvl15_ = ""

enchant15 = ""



def box15():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r2button6.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname15_
        global amount15_

        itemname15_ += str(itemname1.get())
        itemname15_ = itemname15_

        amount15_ += str(amount1.get())
        amount15_ = amount15_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname15_ = ""
        itemname1.delete(0,  END)
        amount15_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant15

        enchant15 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount16_ = ""
itemname16_ = ""

enchantid16_ = ""
lvl16_ = ""

enchant16 = ""



def box16():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r2button7.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname16_
        global amount16_

        itemname16_ += str(itemname1.get())
        itemname16_ = itemname16_

        amount16_ += str(amount1.get())
        amount16_ = amount16_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname16_ = ""
        itemname1.delete(0, END)
        amount16_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant16

        enchant16 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount17_ = ""
itemname17_ = ""

enchantid17_ = ""
lvl17_ = ""

enchant17 = ""



def box17():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r2button8.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname17_
        global amount17_

        itemname17_ += str(itemname1.get())
        itemname17_ = itemname17_

        amount17_ += str(amount1.get())
        amount17_ = amount17_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname17_ = ""
        itemname1.delete(0, END)
        amount17_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant17

        enchant17 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount18_ = ""
itemname18_ = ""

enchantid18_ = ""
lvl18_ = ""

enchant18 = ""



def box18():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r2button9.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname18_
        global amount18_

        itemname18_ += str(itemname1.get())
        itemname18_ = itemname18_

        amount18_ += str(amount1.get())
        amount18_ = amount18_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname18_ = ""
        itemname1.delete(0, END)
        amount18_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant18

        enchant18 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount19_ = ""
itemname19_ = ""

enchantid19_ = ""
lvl19_ = ""

enchant19 = ""



def box19():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r3button1.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname19_
        global amount19_

        itemname19_ += str(itemname1.get())
        itemname19_ = itemname19_

        amount19_ += str(amount1.get())
        amount19_ = amount19_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname19_ = ""
        itemname1.delete(0, END)
        amount19_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant19

        enchant19 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount20_ = ""
itemname20_ = ""

enchantid20_ = ""
lvl20_ = ""

enchant20 = ""



def box20():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r3button2.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname20_
        global amount20_

        itemname20_ += str(itemname1.get())
        itemname20_ = itemname20_

        amount20_ += str(amount1.get())
        amount20_ = amount20_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname20_ = ""
        itemname1.delete(0, END)
        amount20_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant20

        enchant20 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount21_ = ""
itemname21_ = ""

enchantid21_ = ""
lvl21_ = ""

enchant21 = ""



def box21():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r3button3.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname21_
        global amount21_

        itemname21_ += str(itemname1.get())
        itemname21_ = itemname21_

        amount21_ += str(amount1.get())
        amount21_ = amount21_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname21_ = ""
        itemname1.delete(0, END)
        amount21_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant21

        enchant21 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount22_ = ""
itemname22_ = ""

enchantid22_ = ""
lvl22_ = ""

enchant22 = ""



def box22():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r3button4.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname22_
        global amount22_

        itemname22_ += str(itemname1.get())
        itemname22_ = itemname22_

        amount22_ += str(amount1.get())
        amount22_ = amount22_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname22_ = ""
        itemname1.delete(0, END)
        amount22_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant22

        enchant22 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount23_ = ""
itemname23_ = ""

enchantid23_ = ""
lvl23_ = ""

enchant23 = ""



def box23():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r3button5.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname23_
        global amount23_

        itemname23_ += str(itemname1.get())
        itemname23_ = itemname23_

        amount23_ += str(amount1.get())
        amount23_ = amount23_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname23_ = ""
        itemname1.delete(0, END)
        amount23_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant23

        enchant23 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount24_ = ""
itemname24_ = ""

enchantid24_ = ""
lvl24_ = ""

enchant24 = ""



def box24():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r3button6.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname24_
        global amount24_

        itemname24_ += str(itemname1.get())
        itemname24_ = itemname24_

        amount24_ += str(amount1.get())
        amount24_ = amount24_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname24_ = ""
        itemname1.delete(0, END)
        amount24_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant24

        enchant24 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount25_ = ""
itemname25_ = ""

enchantid25_ = ""
lvl25_ = ""

enchant25 = ""



def box25():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r3button7.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname25_
        global amount25_

        itemname25_ += str(itemname1.get())
        itemname25_ = itemname25_

        amount25_ += str(amount1.get())
        amount25_ = amount25_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname25_ = ""
        itemname1.delete(0, END)
        amount25_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant25

        enchant25 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount26_ = ""
itemname26_ = ""

enchantid26_ = ""
lvl26_ = ""

enchant26 = ""



def box26():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r3button8.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname26_
        global amount26_

        itemname26_ += str(itemname1.get())
        itemname26_ = itemname26_

        amount26_ += str(amount1.get())
        amount26_ = amount26_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname26_ = ""
        itemname1.delete(0, END)
        amount26_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant26

        enchant26 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)

amount27_ = ""
itemname27_ = ""

enchantid27_ = ""
lvl27_ = ""

enchant27 = ""



def box27():
    global pop
    pop = Toplevel(kitmaker)
    pop.title("Item Select")
    pop.configure(bg='black')

    font = Font(family="Uni Sans Heavy")  # font

    framebox = LabelFrame(pop, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
    framebox.grid(row=0, column=0, columnspan=2, padx=3, pady=7)

    def submitchoose():
        r3button9.config(bg="green")
        pop.destroy()

    def name_kit():
        global itemname27_
        global amount27_

        itemname27_ += str(itemname1.get())
        itemname27_ = itemname27_

        amount27_ += str(amount1.get())
        amount27_ = amount27_

        enter1.config(text="Clear", command=clear1)

    def clear1():
        itemname27_ = ""
        itemname1.delete(0, END)
        amount27_ = ""
        amount1.delete(0, END)
        pop.destroy()

    def ench_kit():
        global enchant27

        enchant27 += '{id:' + str(enchantid1.get()) +'s,lvl:' + str(lvl1.get()) +'s},'


    # item chose
    itemname1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    itemname1.grid(row=0, column=1, padx=3, pady=7, rowspan=1, sticky="N")
    itemname1.insert(0, "Item Name & Amount")

    # item amount
    amount1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    amount1.grid(row=0, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter item into nbt
    enter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=name_kit)
    enter1.grid(row=0, column=3, padx=3, pady=3, rowspan=1)

    # enter enchants
    enchantid1 = Entry(framebox, width=20, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    enchantid1.grid(row=1, column=1, padx=3, pady=3, )
    enchantid1.insert(0, "Enchant ID & Level")

    # enter enchant lvl
    lvl1 = Entry(framebox, width=5, font=("Uni Sans Heavy", 14), borderwidth=1, bg="black", fg="green")
    lvl1.grid(row=1, column=2, padx=3, pady=7, rowspan=1, sticky="N")

    # enter ench into nbt
    enchenter1 = Button(framebox, height=1, text="Enter", bg="black", fg="green", command=ench_kit)
    enchenter1.grid(row=1, column=3, padx=3, pady=3, rowspan=1)

    submitchoose = Button(framebox, height=1, padx=12, text="Submit", bg="black", fg="green", command=submitchoose)
    submitchoose.grid(row=2, column=1, columnspan=4, padx=3, pady=3, rowspan=1)




def submit():
    global itemname1_
    global amount1_

    if itemname1_ == "":
        itemname1_ = "air"
    if amount1_ == "":
        amount1_ = str(0)

    global itemname2_
    global amount2_

    if itemname2_ == "":
        itemname2_ = "air"
    if amount2_ == "":
        amount2_ = str(0)

    global itemname3_
    global amount3_

    if itemname3_ == "":
        itemname3_ = "air"
    if amount3_ == "":
        amount3_ = str(0)

    global itemname4_
    global amount4_

    if itemname4_ == "":
        itemname4_ = "air"
    if amount4_ == "":
        amount4_ = str(0)

    global itemname5_
    global amount5_

    if itemname5_ == "":
        itemname5_ = "air"
    if amount5_ == "":
        amount5_ = str(0)

    global itemname6_
    global amount6_

    if itemname6_ == "":
        itemname6_ = "air"
    if amount6_ == "":
        amount6_ = str(0)

    global itemname7_
    global amount7_

    if itemname7_ == "":
        itemname7_ = "air"
    if amount7_ == "":
        amount7_ = str(0)

    global itemname8_
    global amount8_

    if itemname8_ == "":
        itemname8_ = "air"
    if amount8_ == "":
        amount8_ = str(0)

    global itemname9_
    global amount9_

    if itemname9_ == "":
        itemname9_ = "air"
    if amount9_ == "":
        amount9_ = str(0)

    global itemname10_
    global amount10_

    if itemname10_ == "":
        itemname10_ = "air"
    if amount10_ == "":
        amount10_ = str(0)

    global itemname11_
    global amount11_

    if itemname11_ == "":
        itemname11_ = "air"
    if amount11_ == "":
        amount11_ = str(0)

    global itemname12_
    global amount12_

    if itemname12_ == "":
        itemname12_ = "air"
    if amount12_ == "":
        amount12_ = str(0)

    global itemname13_
    global amount13_

    if itemname13_ == "":
        itemname13_ = "air"
    if amount13_ == "":
        amount13_ = str(0)

    global itemname14_
    global amount14_

    if itemname14_ == "":
        itemname14_ = "air"
    if amount14_ == "":
        amount14_ = str(0)

    global itemname15_
    global amount15_

    if itemname15_ == "":
        itemname15_ = "air"
    if amount15_ == "":
        amount15_ = str(0)

    global itemname16_
    global amount16_

    if itemname16_ == "":
        itemname16_ = "air"
    if amount16_ == "":
        amount16_ = str(0)

    global itemname17_
    global amount17_

    if itemname17_ == "":
        itemname17_ = "air"
    if amount17_ == "":
        amount17_ = str(0)

    global itemname18_
    global amount18_

    if itemname18_ == "":
        itemname18_ = "air"
    if amount18_ == "":
        amount18_ = str(0)

    global itemname19_
    global amount19_

    if itemname19_ == "":
        itemname19_ = "air"
    if amount19_ == "":
        amount19_ = str(0)

    global itemname20_
    global amount20_

    if itemname20_ == "":
        itemname20_ = "air"
    if amount20_ == "":
        amount20_ = str(0)

    global itemname21_
    global amount21_

    if itemname21_ == "":
        itemname21_ = "air"
    if amount21_ == "":
        amount21_ = str(0)

    global itemname22_
    global amount22_

    if itemname22_ == "":
        itemname22_ = "air"
    if amount22_ == "":
        amount22_ = str(0)

    global itemname23_
    global amount23_

    if itemname23_ == "":
        itemname23_ = "air"
    if amount23_ == "":
        amount23_ = str(0)

    global itemname24_
    global amount24_

    if itemname24_ == "":
        itemname24_ = "air"
    if amount24_ == "":
        amount24_ = str(0)

    global itemname25_
    global amount25_

    if itemname25_ == "":
        itemname25_ = "air"
    if amount25_ == "":
        amount25_ = str(0)

    global itemname26_
    global amount26_

    if itemname26_ == "":
        itemname26_ = "air"
    if amount26_ == "":
        amount26_ = str(0)

    global itemname27_
    global amount27_

    if itemname27_ == "":
        itemname27_ = "air"
    if amount27_ == "":
        amount27_ = str(0)

    global enchant
    global enchant2
    global enchant3
    global enchant4
    global enchant5
    global enchant6
    global enchant7
    global enchant8
    global enchant9
    global enchant10
    global enchant11
    global enchant12
    global enchant13
    global enchant14
    global enchant15
    global enchant16
    global enchant17
    global enchant18
    global enchant19
    global enchant20
    global enchant21
    global enchant22
    global enchant23
    global enchant24
    global enchant25
    global enchant26
    global enchant27

    if enchant == "{id:s,lvl:s},":
        enchant = ""
    if enchant2 == "{id:s,lvl:s},":
        enchant2 = ""
    if enchant3 == "{id:s,lvl:s},":
        enchant3 = ""
    if enchant4 == "{id:s,lvl:s},":
        enchant4 = ""
    if enchant5 == "{id:s,lvl:s},":
        enchant5 = ""
    if enchant6 == "{id:s,lvl:s},":
        enchant6 = ""
    if enchant7 == "{id:s,lvl:s},":
        enchant7 = ""
    if enchant8 == "{id:s,lvl:s},":
        enchant8 = ""
    if enchant9 == "{id:s,lvl:s},":
        enchant9 = ""
    if enchant10 == "{id:s,lvl:s},":
        enchant10 = ""
    if enchant11 == "{id:s,lvl:s},":
        enchant11 = ""
    if enchant12 == "{id:s,lvl:s},":
        enchant12 = ""
    if enchant13 == "{id:s,lvl:s},":
        enchant13 = ""
    if enchant14 == "{id:s,lvl:s},":
        enchant14 = ""
    if enchant15 == "{id:s,lvl:s},":
        enchant15 = ""
    if enchant16 == "{id:s,lvl:s},":
        enchant16 = ""
    if enchant17 == "{id:s,lvl:s},":
        enchant17 = ""
    if enchant18 == "{id:s,lvl:s},":
        enchant18 = ""
    if enchant19 == "{id:s,lvl:s},":
        enchant19 = ""
    if enchant20 == "{id:s,lvl:s},":
        enchant20 = ""
    if enchant20 == "{id:s,lvl:s},":
        enchant20 = ""
    if enchant21 == "{id:s,lvl:s},":
        enchant21 = ""
    if enchant22 == "{id:s,lvl:s},":
        enchant22 = ""
    if enchant23 == "{id:s,lvl:s},":
        enchant23 = ""
    if enchant24 == "{id:s,lvl:s},":
        enchant24 = ""
    if enchant25 == "{id:s,lvl:s},":
        enchant25 = ""
    if enchant26 == "{id:s,lvl:s},":
        enchant26 = ""
    if enchant27 == "{id:s,lvl:s},":
        enchant27 = ""

     # if = empty air 0

    nbt = ('{Count:1b,Damage:' + box_colourentry.get() +
          's,Name:"minecraft:shulker_box",Slot:1b,WasPickedUp:0b,tag:{Items:[{Count:'
           + amount1_ +
          'b,Damage:0s,Name:"minecraft:' + itemname1_ +
          '",Slot:0b,WasPickedUp:0b,tag:{ench:[' + enchant +
           ']}},{Count:' + amount2_ +
           'b,Damage:0s,Name:"minecraft:' + itemname2_ +
           '",Slot:1b,WasPickedUp:0b,tag:{ench:[' + enchant2 +
           ']}},{Count:' + amount3_ +
           'b,Damage:0s,Name:"minecraft:' + itemname3_ +
           '",Slot:2b,WasPickedUp:0b,tag:{ench:[' + enchant3 +
           ']}},{Count:' + amount4_ +
           'b,Damage:0s,Name:"minecraft:' + itemname4_ +
           '",Slot:3b,WasPickedUp:0b,tag:{ench:[' + enchant4 +
           ']}},{Count:' + amount5_ +
           'b,Damage:0s,Name:"minecraft:' + itemname5_ +
           '",Slot:4b,WasPickedUp:0b,tag:{ench:[' + enchant5 +
           ']}},{Count:' + amount6_ +
           'b,Damage:0s,Name:"minecraft:' + itemname6_ +
           '",Slot:5b,WasPickedUp:0b,tag:{ench:[' + enchant6 +
           ']}},{Count:' + amount7_ +
           'b,Damage:0s,Name:"minecraft:' + itemname7_ +
           '",Slot:6b,WasPickedUp:0b,tag:{ench:[' + enchant7 +
           ']}},{Count:' + amount8_ +
           'b,Damage:0s,Name:"minecraft:' + itemname8_ +
           '",Slot:7b,WasPickedUp:0b,tag:{ench:[' + enchant8 +
           ']}},{Count:' + amount9_ +
           'b,Damage:0s,Name:"minecraft:' + itemname9_ +
           '",Slot:8b,WasPickedUp:0b,tag:{ench:[' + enchant9 +
           ']}},{Count:' + amount10_ +
           'b,Damage:0s,Name:"minecraft:' + itemname10_ +
           '",Slot:9b,WasPickedUp:0b,tag:{ench:[' + enchant10 +
           ']}},{Count:' + amount11_ +
           'b,Damage:10s,Name:"minecraft:' + itemname11_ +
           '",Slot:10b,WasPickedUp:0b,tag:{ench:[' + enchant11 +
           ']}},{Count:' + amount12_ +
           'b,Damage:0s,Name:"minecraft:' + itemname12_ +
           '",Slot:11b,WasPickedUp:0b,tag:{ench:[' + enchant12 +
           ']}},{Count:' + amount13_ +
           'b,Damage:0s,Name:"minecraft:' + itemname13_ +
           '",Slot:12b,WasPickedUp:0b,tag:{ench:[' + enchant13 +
           ']}},{Count:' + amount14_ +
           'b,Damage:0s,Name:"minecraft:' + itemname14_ +
           '",Slot:13b,WasPickedUp:0b,tag:{ench:[' + enchant14 +
           ']}},{Count:' + amount15_ +
           'b,Damage:0s,Name:"minecraft:' + itemname15_ +
           '",Slot:14b,WasPickedUp:0b,tag:{ench:[' + enchant15 +
           ']}},{Count:' + amount16_ +
           'b,Damage:0s,Name:"minecraft:' + itemname16_ +
           '",Slot:15b,WasPickedUp:0b,tag:{ench:[' + enchant16 +
           ']}},{Count:' + amount17_ +
           'b,Damage:0s,Name:"minecraft:' + itemname17_ +
           '",Slot:16b,WasPickedUp:0b,tag:{ench:[' + enchant17 +
           ']}},{Count:' + amount18_ +
           'b,Damage:0s,Name:"minecraft:' + itemname18_ +
           '",Slot:17b,WasPickedUp:0b,tag:{ench:[' + enchant18 +
           ']}},{Count:' + amount19_ +
           'b,Damage:0s,Name:"minecraft:' + itemname19_ +
           '",Slot:18b,WasPickedUp:0b,tag:{ench:[' + enchant19 +
           ']}},{Count:' + amount20_ +
           'b,Damage:0s,Name:"minecraft:' + itemname20_ +
           '",Slot:19b,WasPickedUp:0b,tag:{ench:[' + enchant20 +
           ']}},{Count:' + amount21_ +
           'b,Damage:0s,Name:"minecraft:' + itemname21_ +
           '",Slot:20b,WasPickedUp:0b,tag:{ench:[' + enchant21 +
           ']}},{Count:' + amount22_ +
           'b,Damage:0s,Name:"minecraft:' + itemname22_ +
           '",Slot:21b,WasPickedUp:0b,tag:{ench:[' + enchant22 +
           ']}},{Count:' + amount23_ +
           'b,Damage:0s,Name:"minecraft:' + itemname23_ +
           '",Slot:22b,WasPickedUp:0b,tag:{ench:[' + enchant23 +
           ']}},{Count:' + amount24_ +
           'b,Damage:0s,Name:"minecraft:' + itemname24_ +
           '",Slot:23b,WasPickedUp:0b,tag:{ench:[' + enchant24 +
           ']}},{Count:' + amount25_ +
           'b,Damage:0s,Name:"minecraft:' + itemname25_ +
           '",Slot:24b,WasPickedUp:0b,tag:{ench:[' + enchant25 +
           ']}},{Count:' + amount26_ +
           'b,Damage:0s,Name:"minecraft:' + itemname26_ +
           '",Slot:25b,WasPickedUp:0b,tag:{ench:[' + enchant26 +
           ']}},{Count:' + amount27_ +
           'b,Damage:0s,Name:"minecraft:' + itemname27_ +
           '",Slot:26b,WasPickedUp:0b,tag:{ench:[' + enchant27 +
           ']}}],RepairCost:0,display:{Name:"' + box_nameentry.get() +
          '",Lore:["' + box_loreentry.get() + '"]}}}}}}')

    print(nbt)
    pyperclip.copy(nbt)

def clearall():
    global enchant
    global enchant2
    global enchant3
    global enchant4
    global enchant5
    global enchant6
    global enchant7
    global enchant8
    global enchant9
    global enchant10
    global enchant11
    global enchant12
    global enchant13
    global enchant14
    global enchant15
    global enchant16
    global enchant17
    global enchant18
    global enchant19
    global enchant20
    global enchant21
    global enchant22
    global enchant23
    global enchant24
    global enchant25
    global enchant26
    global enchant27

    global itemname1_
    global amount1_

    global itemname2_
    global amount2_

    global itemname3_
    global amount3_

    global itemname4_
    global amount4_

    global itemname5_
    global amount5_

    global itemname6_
    global amount6_

    global itemname7_
    global amount7_

    global itemname8_
    global amount8_

    global itemname9_
    global amount9_

    global itemname10_
    global amount10_

    global itemname11_
    global amount11_

    global itemname12_
    global amount12_

    global itemname13_
    global amount13_

    global itemname14_
    global amount14_

    global itemname15_
    global amount15_

    global itemname16_
    global amount16_

    global itemname17_
    global amount17_

    global itemname18_
    global amount18_

    global itemname19_
    global amount19_

    global itemname20_
    global amount20_

    global itemname21_
    global amount21_

    global itemname22_
    global amount22_

    global itemname23_
    global amount23_

    global itemname24_
    global amount24_

    global itemname25_
    global amount25_

    global itemname26_
    global amount26_

    global itemname27_
    global amount27_

    global box_colourentry
    global box_loreentry
    global box_nameentry

    enchant = ""
    enchant3 = ""
    enchant4 = ""
    enchant5 = ""
    enchant6 = ""
    enchant7 = ""
    enchant8 = ""
    enchant9 = ""
    enchant10 = ""
    enchant11 = ""
    enchant12 = ""
    enchant13 = ""
    enchant14 = ""
    enchant15 = ""
    enchant16 = ""
    enchant17 = ""
    enchant18 = ""
    enchant19 = ""
    enchant20 = ""
    enchant21 = ""
    enchant22 = ""
    enchant23 = ""
    enchant24 = ""
    enchant25 = ""
    enchant26 = ""
    enchant26 = ""
    enchant27 = ""

    itemname1_ = ""
    itemname2_ = ""
    itemname3_ = ""
    itemname4_ = ""
    itemname5_ = ""
    itemname6_ = ""
    itemname7_ = ""
    itemname8_ = ""
    itemname9_ = ""
    itemname10_ = ""
    itemname11_ = ""
    itemname12_ = ""
    itemname13_ = ""
    itemname14_ = ""
    itemname15_ = ""
    itemname16_ = ""
    itemname17_ = ""
    itemname18_ = ""
    itemname19_ = ""
    itemname20_ = ""
    itemname21_ = ""
    itemname22_ = ""
    itemname23_ = ""
    itemname24_ = ""
    itemname25_ = ""
    itemname26_ = ""
    itemname27_ = ""

    amount1_ = ""
    amount2_ = ""
    amount3_ = ""
    amount4_ = ""
    amount5_ = ""
    amount6_ = ""
    amount7_ = ""
    amount8_ = ""
    amount9_ = ""
    amount10_ = ""
    amount11_ = ""
    amount12_ = ""
    amount13_ = ""
    amount14_ = ""
    amount15_ = ""
    amount16_ = ""
    amount17_ = ""
    amount18_ = ""
    amount19_ = ""
    amount20_ = ""
    amount21_ = ""
    amount22_ = ""
    amount23_ = ""
    amount24_ = ""
    amount25_ = ""
    amount26_ = ""
    amount27_ = ""

    box_colourentry.delete(0, END)
    box_loreentry.delete(0, END)
    box_nameentry.delete(0, END)

    r1button1.config(bg="black")
    r1button2.config(bg="black")
    r1button3.config(bg="black")
    r1button4.config(bg="black")
    r1button5.config(bg="black")
    r1button6.config(bg="black")
    r1button7.config(bg="black")
    r1button8.config(bg="black")
    r1button9.config(bg="black")

    r2button1.config(bg="black")
    r2button2.config(bg="black")
    r2button3.config(bg="black")
    r2button4.config(bg="black")
    r2button5.config(bg="black")
    r2button6.config(bg="black")
    r2button7.config(bg="black")
    r2button8.config(bg="black")
    r2button9.config(bg="black")

    r3button1.config(bg="black")
    r3button2.config(bg="black")
    r3button3.config(bg="black")
    r3button4.config(bg="black")
    r3button5.config(bg="black")
    r3button6.config(bg="black")
    r3button7.config(bg="black")
    r3button8.config(bg="black")
    r3button9.config(bg="black")



font = Font(family="Uni Sans Heavy")  # font

framekit = LabelFrame(frame_tabkit, text="NBT Builder - Caplini", padx=15, pady=5, font=font, bg="black", fg="green")
framekit.grid(row=0, column=1, padx=3, pady=7, sticky="s")

frameoptions = LabelFrame(frame_tabkit, text="Options", padx=15, pady=5, font=font, bg="black", fg="green")
frameoptions.grid(row=0, column=2, padx=3, pady=7, sticky="s")

r1button1 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box1)
r1button1.grid(row=0, column=0, padx=5, pady=5)

r1button2 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box2)
r1button2.grid(row=0, column=1, padx=5, pady=5)

r1button3 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box3)
r1button3.grid(row=0, column=2, padx=5, pady=5)

r1button4 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box4)
r1button4.grid(row=0, column=3, padx=5, pady=5)

r1button5 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box5)
r1button5.grid(row=0, column=4, padx=5, pady=5)

r1button6 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box6)
r1button6.grid(row=0, column=5, padx=5, pady=5)

r1button7 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box7)
r1button7.grid(row=0, column=6, padx=5, pady=5)

r1button8 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box8)
r1button8.grid(row=0, column=7, padx=5, pady=5)

r1button9 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box9)
r1button9.grid(row=0, column=8, padx=5, pady=5)

r2button1 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box10)
r2button1.grid(row=1, column=0, padx=5, pady=5)

r2button2 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box11)
r2button2.grid(row=1, column=1, padx=5, pady=5)

r2button3 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box12)
r2button3.grid(row=1, column=2, padx=5, pady=5)

r2button4 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box13)
r2button4.grid(row=1, column=3, padx=5, pady=5)

r2button5 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box14)
r2button5.grid(row=1, column=4, padx=5, pady=5)

r2button6 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box15)
r2button6.grid(row=1, column=5, padx=5, pady=5)

r2button7 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box16)
r2button7.grid(row=1, column=6, padx=5, pady=5)

r2button8 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box17)
r2button8.grid(row=1, column=7, padx=5, pady=5)

r2button9 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box18)
r2button9.grid(row=1, column=8, padx=5, pady=5)

r3button1 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box19)
r3button1.grid(row=2, column=0, padx=5, pady=5)

r3button2 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box20)
r3button2.grid(row=2, column=1, padx=5, pady=5)

r3button3 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box21)
r3button3.grid(row=2, column=2, padx=5, pady=5)

r3button4 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box22)
r3button4.grid(row=2, column=3, padx=5, pady=5)

r3button5 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box23)
r3button5.grid(row=2, column=4, padx=5, pady=5)

r3button6 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box24)
r3button6.grid(row=2, column=5, padx=5, pady=5)

r3button7 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box25)
r3button7.grid(row=2, column=6, padx=5, pady=5)

r3button8 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box26)
r3button8.grid(row=2, column=7, padx=5, pady=5)

r3button9 = Button(framekit, height=20, width=30, font=("Uni Sans Heavy", 1), bg="black", fg="green", command=box27)
r3button9.grid(row=2, column=8, padx=5, pady=5)

# box colour
box_colour = Label(frameoptions, text="Colour:", font=font, bg="black", fg="green")
box_colour.grid(row=0, column=0, padx=5, pady=5)
box_colourentry = Entry(frameoptions, font=font, bg="black", fg="green")
box_colourentry.grid(row=0, column=1, padx=5, pady=5)

# box&Item lore
box_lore = Label(frameoptions, text="Lore:", font=font, bg="black", fg="green")
box_lore.grid(row=1, column=0, padx=5, pady=5)
box_loreentry = Entry(frameoptions, font=font, bg="black", fg="green")
box_loreentry.grid(row=1, column=1, padx=5, pady=5)

# box name
box_name = Label(frameoptions, text="Box Name:", font=font, bg="black", fg="green")
box_name.grid(row=2, column=0, padx=5, pady=5)
box_nameentry = Entry(frameoptions, font=font, bg="black", fg="green")
box_nameentry.grid(row=2, column=1, padx=5, pady=5)

# submit
submit = Button(frameoptions, width=12, text="Submit", font=font, bg="black", fg="green", command=submit)
submit.grid(row=3, column=1, padx=5, pady=5)

clearwhole = Button(frameoptions, width=12, text="clear all", font=font, bg="black", fg="green", command=clearall)
clearwhole.grid(row=3, column=0, padx=5, pady=5)

Caplini = Label(frame_tabkit, text="By Caplini", font=("Uni Sans Heavy", 100), bg="black", fg="green")
Caplini.grid(row=1, column=1, columnspan=10, rowspan=10, sticky="n")

root.mainloop()
