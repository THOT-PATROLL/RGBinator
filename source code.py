from tkinter import *


#glowing melee template
##########################################################################################
##########################################################################################
def glow_melee_menue():
    win = Tk()
#input for projects name
    label = Label(win, text="insert project name")
    label.grid(row=0, column=0)
    project_name = Entry(win, bg='light grey')
    project_name.grid(row=1, column=0)

    #input for the file path
    label = Label(win, text="insert file path")
    label.grid(row=2, column=0)
    file_path = Entry(win, bg='light grey')
    file_path.grid(row=3, column=0)

    #name of the object name
    label = Label(win, text="insert object name")
    label.grid(row=4, column=0)
    texture_name = Entry(win, bg='light grey')
    texture_name.grid(row=5, column=0)

    #insert the name of the material that you will be editing
    label = Label(win, text="material name")
    label.grid(row=6, column=0)
    material_name = Entry(win, bg='light grey')
    material_name.grid(row=7, column=0)

    #insert the name of the config file
    label = Label(win, text="config file")
    label.grid(row=8, column=0)
    config_file = Entry(win, bg='light grey')
    config_file.grid(row=9, column=0)


##########################################print to console for glowing melee
    def print_console_melee_glow():
        path = file_path.get()
        path = path.replace('\\', '/')
        print('''


    ''')
        print('''----------------------------------------------------------------
<materials version="3" group="melee_group">
    <material unique="true" render_template="generic:DEPTH_SCALING:DIFFUSE_TEXTURE:NORMALMAP:NORMALMAP_UV1:SELF_ILLUMINATION:SELF_ILLUMINATION_BLOOM" name="'''+material_name.get()+'''" version="2">
        <diffuse_texture file="'''+path+"/"+texture_name.get()+'''_df"/>
        <bump_normal_texture file="'''+path+"/"+texture_name.get()+'''_nm"/>
        <self_illumination_texture file="'''+path+"/"+texture_name.get()+'''_il"/>
        <variable type="scalar" name="il_bloom" value="9.999000474927"/>
        <variable type="scalar" name="il_multiplier" value="reddot"/>
    </material>
</materials>
----------------------------------------------------------------
copy the text above and replace the part of the config file that you made this for with it''')

#######################################generate main.xml for glowing melee
    def generate_melee_glow_main():
        path = file_path.get()
        path = path.replace('\\', '/')
        name = project_name.get()
        add = open("add.xml", "x")
        add.write('''<table name="'''+name+'''">
        <texture path="'''+path+"/"+texture_name.get()+'''_il"/>
</table>''')
        

    label6 = Label(win, text="")
    label6.grid(row=0, column=2)
    print_console = Button(win, bg='light grey', text="print config file", command=print_console_melee_glow)
    print_console.grid(row=1, column=2)

    label7 = Label(win, text='')
    label7.grid(row=2, column=2)
    add_xml = Button(win, bg='light grey', text='generate "add.xml"', command=generate_melee_glow_main)
    add_xml.grid(row=3, column=2)


    win.mainloop()






#copy and pasted code from melee menue, needs to be changed for glove purposes 
##########################################################################################
##########################################################################################
def glove_glow_menue():
    win = Tk()
#input for projects name
    label = Label(win, text="insert project name")
    label.grid(row=0, column=0)
    project_name = Entry(win, bg='light grey')
    project_name.grid(row=1, column=0)

    #input for the file path
    label = Label(win, text="insert file path")
    label.grid(row=2, column=0)
    file_path = Entry(win, bg='light grey')
    file_path.grid(row=3, column=0)

    #name of the object name
    label = Label(win, text="insert object name")
    label.grid(row=4, column=0)
    texture_name = Entry(win, bg='light grey')
    texture_name.grid(row=5, column=0)

    #insert the name of the material that you will be editing
    label = Label(win, text="material name")
    label.grid(row=6, column=0)
    material_name = Entry(win, bg='light grey')
    material_name.grid(row=7, column=0)

    #insert the name of the config file
    label = Label(win, text="group name")
    label.grid(row=8, column=0)
    group = Entry(win, bg='light grey')
    group.grid(row=9, column=0)




########################################generate main.xml for gloves
    def generate_melee_glow_main():
        path = file_path.get()
        path = path.replace('\\', '/')
        name = project_name.get()
        add = open("add.xml", "x")
        add.write('''<table name="'''+name+'''">
        <texture path="'''+path+"/"+texture_name.get()+'''_il"/>
</table>''')
#########################################print to console for gloves
        #########################################
        #########################################
    def print_console_glove_glow():
        path = file_path.get()
        path = path.replace('\\', '/')
        group_name = group.get()
        print('''


    ''')
        print('''----------------------------------------------------------------
<materials version="3" group="'''+group_name+'''">
    <material render_template="generic:DEPTH_SCALING:DIFFUSE_TEXTURE:NORMALMAP:SELF_ILLUMINATION:SELF_ILLUMINATION_BLOOM:SKINNED_3WEIGHTS" name="'''+material_name.get()+'''" version="2">
        <diffuse_texture file="'''+path+"/"+texture_name.get()+'''_df"/>
        <bump_normal_texture file="'''+path+"/"+texture_name.get()+'''_nm"/>
        <self_illumination_texture file="'''+path+"/"+texture_name.get()+'''_il"/>
        <variable type="scalar" name="il_bloom" value="9.9750004737871"/>
        <variable type="scalar" name="il_multiplier" value="reddot"/>
    </material>
    <material name="shadow_caster" render_template="shadow_caster_only:SKINNED_1WEIGHT"/>
</materials>
''')
    def print_console_glove_glow_third():
        path = file_path.get()
        path = path.replace('\\', '/')
        group_name = group.get()
        print('''


    ''')
        print('''<materials version="3" group="'''+group_name+'''">
    <material unique="true" render_template="generic:CONTOUR:DIFFUSE_TEXTURE:NORMALMAP:SELF_ILLUMINATION:SELF_ILLUMINATION_BLOOM:SKINNED_3WEIGHTS" name="'''+material_name.get()+'''" version="2">
        <diffuse_texture              file="'''+path+"/"+texture_name.get()+'''_df"/>
        <bump_normal_texture          file="'''+path+"/"+texture_name.get()+'''_nm"/>
        <variable type="scalar" name="il_multiplier" value="match"/>
        <self_illumination_texture    file="'''+path+"/"+texture_name.get()+'''_il"/>
        <variable type="scalar" name="il_bloom" value="9.999000474927"/>
        <variable name="contour_color" value="0 0 0" type="vector3"/>
        <variable name="contour_opacity" value="1" type="scalar"/>
        <variable name="contour_distance"  value="0" type="scalar"/>
    </material>
    <material name="shadow_caster" render_template="shadow_caster_only:SKINNED_1WEIGHT"/>
</materials>
''')

    label6 = Label(win, text="")
    label6.grid(row=0, column=2)
    print_console = Button(win, bg='light grey', text="print config file", command=print_console_glove_glow)
    print_console.grid(row=1, column=2)

    label8 = Label(win, text="")
    label8.grid(row=2, column=2)
    print_third = Button(win, bg='light grey', text="print third config", command=print_console_glove_glow_third)
    print_third.grid(row=3, column=2)

    label7 = Label(win, text='')
    label7.grid(row=4, column=2)
    add_xml = Button(win, bg='light grey', text='generate "add.xml"', command=generate_melee_glow_main)
    add_xml.grid(row=5, column=2)

    
    



#code for the pick mod type menue
##########################################################################################
choose_type = Tk()
choose_type.title('type picker')
choose_type.geometry('240x100')
label = Label(choose_type, text= 'choose what kind of mod you want to make')
label.pack()

print_console = Button(choose_type, bg='light grey', text="simple glowing melee", command=glow_melee_menue, relief = GROOVE)
print_console.pack()

glove = Button(choose_type,  bg='light grey', text="simple glowing glove", command=glove_glow_menue, relief = GROOVE)
glove.pack()
input("dont press enter here lol idk why but it breaks it")
