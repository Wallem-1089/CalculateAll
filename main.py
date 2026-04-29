from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.picker import MDThemePicker
from kivymd.toast import toast
from statistics import mean, median, mode
from kivy.core.window import Window
from math import pi, fmod, sqrt, log10, e, exp, log, factorial as fact
import math
import numpy as np

Window.size = (340, 500)


def rad_to_deg(angle):
    deg = (pi / 180) * angle
    return deg


def ln(x):
    return log(x, e)


def per(x):
    return x * 1 / 100


def sin(x):
    res = math.sin(rad_to_deg(x))
    return res


def sin_r(x):
    res = math.sin(x)
    return res


def cos(x):
    res = math.cos(rad_to_deg(x))
    return res


def cos_r(x):
    res = math.cos(x)
    return res


def tan(x):
    res = math.tan(rad_to_deg(x))
    return res


def tan_r(x):
    res = math.tan(x)
    return res


def asin(x):
    res = math.asin(rad_to_deg(x))
    return res


def asin_r(x):
    res = math.asin(x)
    return res


def acos(x):
    res = math.acos(rad_to_deg(x))
    return res


def acos_r(x):
    res = math.acos(x)
    return res


def atan(x):
    res = math.atan(rad_to_deg(x))
    return res


def atan_r(x):
    res = math.atan(x)
    return res


screen_helper = '''
Screen:
    NavigationLayout:
        ScreenManager:
            id: screen_manager
            Screen:
                name: 'screen_one'
                id: screen_one
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Standard'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    TextInput:
                        id: show
                        multiline: False
                        readonly:True
                        halign: 'right'
                        font_size: 25
                    BoxLayout:
                        orientation: 'horizontal'
                        height: '96dp'
                        spacing: '70dp'
                        padding: '8dp'
                        size_hint_y: None
                        MDTextButton:
                            id: seven
                            text: '7'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 50
                            on_release: app.on_button_press(seven)
                        MDTextButton:
                            id: eight
                            text: '8'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 50
                            on_release: app.on_button_press(eight)
                        MDTextButton:
                            id: nine
                            text: '9'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 50
                            on_release: app.on_button_press(nine)
                        MDIconButton:
                            id: division_sign
                            icon: 'division'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.on_button_press(division_sign)
                    BoxLayout:
                        orientation: 'horizontal'
                        height: '96dp'
                        spacing: '70dp'
                        padding: '8dp'
                        size_hint_y: None
                        MDTextButton:
                            id: four
                            text: '4'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 50
                            on_release: app.on_button_press(four)
                        MDTextButton:
                            id: five
                            text: '5'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 50
                            on_release: app.on_button_press(five)
                        MDTextButton:
                            id: six
                            text: '6'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 50
                            on_release: app.on_button_press(six)
                        MDIconButton:
                            id: multiply_sign
                            icon: 'close'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.on_button_press(multiply_sign)
                    BoxLayout:
                        orientation: 'horizontal'
                        height: '94dp'
                        spacing: '70dp'
                        padding: '8dp'
                        size_hint_y: None
                        MDTextButton:
                            id: one
                            text: '1'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 50
                            on_release: app.on_button_press(one)
                        MDTextButton:
                            id: two
                            text: '2'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 50
                            on_release: app.on_button_press(two)
                        MDTextButton:
                            id: three
                            text: '3'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 50
                            on_release: app.on_button_press(three)
                        MDIconButton:
                            id: minus_sign
                            icon: 'minus'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.on_button_press(minus_sign)
                    BoxLayout:
                        orientation: 'horizontal'
                        height: '50dp'
                        spacing: '54dp'
                        padding: '8dp'
                        size_hint_y: None
                        MDTextButton:
                            id: zero
                            text: '0'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.on_button_press(zero)
                            font_size: 50
                        MDTextButton:
                            id: clear
                            text: ' C'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 50
                            on_release: app.clear_screen()
                        MDTextButton:
                            id: decimal_point
                            text: '  .  '
                            font_size: 50
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.on_button_press(decimal_point)
                        MDIconButton:
                            id: plus_sign
                            icon: 'plus'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.on_button_press(plus_sign)
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            on_release: app.on_solution()
                        Widget:
                        MDTextButton:
                            text: '>'
                            font_size: 35
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            on_release: 
                                screen_manager.current = 'screen_2'
            Screen:
                name: 'screen_2'
                BoxLayout:
                    orientation: 'vertical'
                    BoxLayout:
                        orientation: 'horizontal'
                        spacing: '78dp'
                        MDTextButton:
                            id: inv
                            text: 'INV'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: screen_manager.current = 'screen_3'
                        MDTextButton:
                            id: deg
                            text: 'DEG'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(deg)
                        MDTextButton:
                            id: percent
                            text: ' %'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(percent)
                        Widget:
                    BoxLayout:
                        spacing: '84dp'
                        MDTextButton:
                            id: sin
                            text: 'sin'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(sin)
                        MDTextButton:
                            id: cos
                            text: 'cos'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(cos)
                        MDTextButton:
                            id: tan
                            text: 'tan'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(tan)
                    BoxLayout:
                        spacing: '98dp'
                        MDTextButton:
                            id: In
                            text: 'In'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(In)
                        MDTextButton:
                            id: log
                            text: 'log'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(log)
                        MDTextButton:
                            id: combination
                            text: ' !'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(combination)
                    BoxLayout:
                        spacing: '100dp'
                        MDTextButton:
                            id: pi
                            text: 'π'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.on_button_press(pi)
                            font_size: 25
                        MDTextButton:
                            id: e
                            text: '  e'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(e)
                        MDTextButton:
                            id: to_power
                            text: '   ^'
                            font_size: 25
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.on_button_press(to_power)
                    BoxLayout:
                        spacing: '100dp'
                        MDTextButton:
                            id: front_bracket
                            text: '('
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.on_button_press(front_bracket)
                            font_size: 25
                        MDTextButton:
                            id: end_bracket
                            text: '   )'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(end_bracket)
                        MDTextButton:
                            id: sq_root
                            text: '    √'
                            font_size: 25
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.on_button_press(sq_root)
                    MDIconButton:
                        icon: 'close'
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        on_release: screen_manager.current = 'screen_one'
            Screen:
                name: 'screen_3'
                BoxLayout:
                    orientation: 'vertical'
                    BoxLayout:
                        orientation: 'horizontal'
                        spacing: '78dp'
                        MDTextButton:
                            id: inv
                            text: 'INV'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: screen_manager.current = 'screen_2'
                        MDTextButton:
                            id: deg_two
                            text: 'DEG'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 23
                            on_release: app.on_button_press(deg_two)
                        MDTextButton:
                            id: percent
                            text: '  %'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(percent)
                        Widget:
                    BoxLayout:
                        spacing: '60dp'
                        MDTextButton:
                            id: sin_inv
                            text: 'sin-1'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(sin_inv)
                        MDTextButton:
                            id: cos_inv
                            text: 'cos-1'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(cos_inv)
                        MDTextButton:
                            id: tan_inv
                            text: 'tan-1'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(tan_inv)
                    BoxLayout:
                        spacing: '80dp'
                        MDTextButton:
                            id: e_to_power_x
                            text: 'e^x'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(e_to_power_x)
                        MDTextButton:
                            id: anti_log
                            text: '10^x'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(anti_log)
                        MDTextButton:
                            id: combination
                            text: '   !'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(combination)
                    BoxLayout:
                        spacing: '100dp'
                        MDTextButton:
                            id: pi
                            text: 'π'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.on_button_press(pi)
                            font_size: 25
                        MDTextButton:
                            id: e
                            text: '  e'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(e)
                        MDTextButton:
                            id: to_power
                            text: '   ^'
                            font_size: 25
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.on_button_press(to_power)
                    BoxLayout:
                        spacing: '90dp'
                        MDTextButton:
                            id: front_bracket
                            text: '( '
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.on_button_press(front_bracket)
                            font_size: 25
                        MDTextButton:
                            id: end_bracket
                            text: '    )'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            font_size: 25
                            on_release: app.on_button_press(end_bracket)
                        MDTextButton:
                            id: squared
                            text: '    x^2'
                            font_size: 25
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.on_button_press(squared)
                    MDIconButton:
                        icon: 'close'
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        on_release: screen_manager.current = 'screen_one'           
            Screen:
                name: 'perimeter_screen'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Rectangle'
                            on_release:
                                screen_manager.current = 'perimeter_rectangle'
                        OneLineListItem:
                            text: 'Square'
                            on_release: 
                                screen_manager.current = 'perimeter_square'
                        OneLineListItem:
                            text: 'Triangle'
                            on_release:
                                screen_manager.current = 'perimeter_triangle'
                        OneLineListItem:
                            text: 'Circle'
                            on_release:
                                screen_manager.current = 'perimeter_circle'
                        OneLineListItem:
                            text: 'Parallelogram'
                            on_release:
                                screen_manager.current = 'perimeter_parallelogram'
                        OneLineListItem:
                            text: 'Trapezium'
                            on_release:
                                screen_manager.current = 'perimeter_trapezium'
                        OneLineListItem:
                            text: 'Arc'
                            on_release:
                                screen_manager.current = 'perimeter_arc'
            Screen:
                name: 'area_screen'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Rectangle'
                            on_release:
                                screen_manager.current = 'area_rectangle'
                        OneLineListItem:
                            text: 'Square'
                            on_release:
                                screen_manager.current = 'area_square'
                        OneLineListItem:
                            text: 'Triangle'
                            on_release:
                                screen_manager.current = 'area_triangle'
                        OneLineListItem:
                            text: 'Circle'
                            on_release:
                                screen_manager.current = 'area_circle'
                        OneLineListItem:
                            text: 'Parallelogram'
                            on_release:
                                screen_manager.current = 'area_parallelogram'
                        OneLineListItem:
                            text: 'Trapezium'
                            on_release:
                                screen_manager.current = 'area_trapezium'
                        OneLineListItem:
                            text: 'Sector'
                            on_release:
                                screen_manager.current = 'area_sector'
                        OneLineListItem:
                            text: 'Rhombus'
                            on_release:
                                screen_manager.current = 'area_rhombus'           
            Screen:
                name: 'volume_screen'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Cube'
                            on_release:
                                screen_manager.current = 'volume_cube'
                        OneLineListItem:
                            text: 'Cuboid'
                            on_release:
                                screen_manager.current = 'volume_cuboid'
                        OneLineListItem:
                            text: 'Cylinder'
                            on_release:
                                screen_manager.current = 'volume_cylinder'
                        OneLineListItem:
                            text: 'Cone'
                            on_release:
                                screen_manager.current = 'volume_cone'
                        OneLineListItem:
                            text: 'Square based Pyramid'
                            on_release:
                                screen_manager.current = 'volume_square_based_pyramid'
                        OneLineListItem:
                            text: 'Sphere'
                            on_release:
                                screen_manager.current = 'volume_sphere'
            Screen:
                name: 'surface_area'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Cube'
                            on_release:
                                screen_manager.current = 'surface_area_cube'
                        OneLineListItem:
                            text: 'Cuboid'
                            on_release:
                                screen_manager.current = 'surface_area_cuboid'
                        OneLineListItem:
                            text: 'Cylinder'
                            on_release:
                                screen_manager.current = 'surface_area_cylinder'
                        OneLineListItem:
                            text: 'Sphere'
                            on_release:
                                screen_manager.current = 'surface_area_sphere'
                        OneLineListItem:
                            text: 'Cone'
                            on_release:
                                screen_manager.current = 'surface_area_cone'
            Screen:
                name: 'series_and_sequences'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'nth term(Linear Sequence)'
                            on_release:
                                screen_manager.current = 'nth term(Linear Sequence)'
                        OneLineListItem:
                            text: 'Arithmetic Mean'
                            on_release:
                                screen_manager.current = 'arithmetic_mean'
                        OneLineListItem:
                            text: 'Sum of n terms(Linear Sequence)'
                            on_release:
                                screen_manager.current = 'Sum of n terms(Linear Sequence)'
                        OneLineListItem:
                            text: 'nth term(Geometric Progression)'
                            on_release:
                                screen_manager.current = 'nth term(Geometric Progression)'
                        OneLineListItem:
                            text: 'Geometric mean'
                            on_release:
                                screen_manager.current = 'Geometric mean'
                        OneLineListItem:
                            text: 'Sum of n terms(Geometric Progression)'
                            on_release:
                                screen_manager.current = 'Sum of n terms(Geometric Progression)'
                        OneLineListItem:
                            text: 'Sum to Infinity'
                            on_release:
                                screen_manager.current = 'Sum to Infinity'  
            Screen:
                name: 'simple_interest'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Simple Interest'
                            on_release:
                                screen_manager.current = 'Simple Interest'
                        OneLineListItem:
                            text: 'Rate'
                            on_release:
                                screen_manager.current = 'Rate'
                        OneLineListItem:
                            text: 'Time'
                            on_release:
                                screen_manager.current = 'Time'
                        OneLineListItem:
                            text: 'Principal'
                            on_release:
                                screen_manager.current = 'Principal'
            Screen:
                name: 'compound_interest'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Compound Interest'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Principal'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: compound_interest_p
                        hint_text: 'enter principal here'
                        helper_text: '= principal'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Rate'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: compound_interest_r
                        hint_text: 'enter rate here'
                        helper_text: '= rate'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Number of years'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: compound_interest_n
                        hint_text: 'enter number of years here'
                        helper_text: '= number of years'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_compound_interest()
                        Widget:
                    TextInput:
                        id: compound_interest_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'angles'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Sum of Interior Angles'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Number of Sides'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: sum_of_interior_angles_sides
                        hint_text: 'enter numbers of sides'
                        helper_text: '= numbers of sides'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_sum_of_interior_angles()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: sum_of_interior_angles_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'equations'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Linear Equation'
                            on_release:
                                screen_manager.current = 'linear_equation'
                        OneLineListItem:
                            text: 'Quadratic Equation'
                            on_release:
                                screen_manager.current = 'quadratic_equation'
                        OneLineListItem:
                            text: 'Simultaneous Equation'
                            on_release:
                                screen_manager.current = 'simultaneous_equation'
                        OneLineListItem:
                            text: 'Quadratic equation from roots'
                            on_release:
                                screen_manager.current = 'quadratic_equations_from_roots'
            Screen:
                name: 'modular_arithmetic'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Modular Arithmetic'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Enter the Number'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: modular_arithmetic_number
                        hint_text: 'enter number here'
                        helper_text: '= number'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Enter the mod()'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: modular_arithmetic_mod
                        hint_text: 'enter mod here'
                        helper_text: '= mod'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_modular_arithmetic()
                        Widget:
                    Widget:
                    TextInput:
                        id: modular_arithmetic_text_input    
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'Distance,Time and Speed'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Distance'
                            on_release:
                                screen_manager.current = 'distance'
                        OneLineListItem:
                            text: 'Time'
                            on_release:
                                screen_manager.current = 'time'
                        OneLineListItem:
                            text: 'Speed'
                            on_release:
                                screen_manager.current = 'speed'
            Screen:
                name: 'pythagoras_theorem'
                BoxLayout:
                    orientation: 'vertical'
                    MDLabel:
                        text: 'Do you have the value for the two sides.'
                        font_style: 'H4'
                    BoxLayout:
                        orientation: 'horizontal'
                        Widget:
                        MDRaisedButton:
                            text: 'Yes'
                            on_release:
                                screen_manager.current = 'which_pythagoras'
                        Widget:
                        MDRaisedButton:
                            text: 'No'
                            on_release: 
                                screen_manager.current = 'trigonometrical_ratios'
                        Widget:
                    Widget:
                    Widget:
            Screen:
                name: 'which_pythagoras'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Which do you need to find'
                        OneLineListItem:
                            text: 'Hypotenuse'
                            on_release:
                                screen_manager.current = 'two_side_hypotenuse'
                        OneLineListItem:
                            text: 'Opposite'
                            on_release:
                                screen_manager.current = 'two_side_opposite'
                        OneLineListItem:
                            text: 'Adjacent'
                            on_release:
                                screen_manager.current = 'two_side_adjacent'
            Screen:
                name: 'two_side_hypotenuse'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'To Find Hypotenuse'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Opposite'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: two_side_hypotenuse_opposite
                        hint_text: 'enter opposite here'
                        helper_text: '= opposite'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Adjacent'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: two_side_hypotenuse_adjacent
                        hint_text: 'enter adjacent here'
                        helper_text: '= adjacent'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_pythagoras_theorem_two_side_hypotenuse()
                        Widget:
                    Widget:
                    TextInput:
                        id: pythagoras_theorem_two_side_hypotenuse_text_input    
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'two_side_opposite'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'To Find Opposite'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Adjacent'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: two_side_opposite_adjacent
                        hint_text: 'enter adjacent here'
                        helper_text: '= adjacent'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Hypotenuse'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: two_side_opposite_hypotenuse
                        hint_text: 'enter hypotenuse here'
                        helper_text: '= hypotenuse'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_pythagoras_theorem_two_side_opposite()
                        Widget:
                    Widget:
                    TextInput:    
                        id: pythagoras_theorem_two_side_opposite_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'two_side_adjacent'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'To Find Adjacent'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Opposite'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: two_side_adjacent_opposite
                        hint_text: 'enter opposite here'
                        helper_text: '= opposite'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Hypotenuse'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: two_side_adjacent_hypotenuse
                        hint_text: 'enter hypotenuse here'
                        helper_text: '= hypotenuse'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_pythagoras_theorem_two_side_adjacent()
                        Widget:
                    Widget:
                    TextInput:
                        id: pythagoras_theorem_two_side_adjacent_text_input    
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'trigonometrical_ratios'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Using Trigonometrical ratios to find'
                        OneLineListItem:
                            text: 'Opposite'
                            on_release: 
                                screen_manager.current = 'trigonometrical_ratios_opposite'
                        OneLineListItem:
                            text: 'Hypotenuse'
                            on_release:
                                screen_manager.current = 'trigonometrical_ratios_hypotenuse'
                        OneLineListItem:
                            text: 'Adjacent'
                            on_release:
                                screen_manager.current = 'trigonometrical_ratios_adjacent'
            Screen: 
                name: 'trigonometrical_ratios_opposite'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Which do you have the value for'
                        OneLineListItem:
                            text: 'Hypotenuse'
                            on_release: 
                                screen_manager.current = 'trigonometrical_ratios_opposite_which_hyp'
                        OneLineListItem:
                            text: 'Adjacent'
                            on_release:
                                screen_manager.current = 'trigonometrical_ratios_opposite_which_adj'
            Screen:
                name: 'trigonometrical_ratios_opposite_which_hyp'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Opposite(Trig.ratios)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel:
                        text: 'RAD   DEG'
                        halign: 'right'
                    BoxLayout:
                        orientation: 'horizontal'
                        Widget:
                        Widget:
                        MDCheckbox:
                            id: trig_opp_hyp_rad_checkbox
                            size_hint: None, None
                            size: dp(40), dp(40)
                            pos_hint: {'center_x': .4, 'center_y': .91}
                            halign: 'right'
                            active: True
                            on_active:
                                trig_opp_hyp_deg_checkbox.active = False 
                        MDCheckbox:
                            id: trig_opp_hyp_deg_checkbox
                            size_hint: None, None
                            size: dp(40), dp(40)
                            pos_hint: {'center_x': .4, 'center_y': .91}
                            halign: 'right'
                            active: False
                            on_active:
                                trig_opp_hyp_rad_checkbox.active = False
                    MDLabel: 
                        text: 'Hypotenuse'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: trigonometrical_ratios_opposite_which_hyp_hypotenuse
                        hint_text: 'enter hypotenuse here'
                        helper_text: '= hypotenuse'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Angle'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: trigonometrical_ratios_opposite_which_hyp_angle
                        hint_text: 'enter angle here'
                        helper_text: '= angle'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_trigonometrical_ratios_opposite_which_hyp()
                        Widget:
                    TextInput:
                        id: trigonometrical_ratios_opposite_which_hyp_text_input    
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
                    Widget:
            Screen:
                name: 'trigonometrical_ratios_opposite_which_adj'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Opposite(Trig.ratios)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel:
                        text: 'RAD   DEG'
                        halign: 'right'
                    BoxLayout:
                        orientation: 'horizontal'
                        Widget:
                        Widget:
                        MDCheckbox:
                            id: trig_opp_adj_rad_checkbox
                            size_hint: None, None
                            size: dp(40), dp(40)
                            pos_hint: {'center_x': .4, 'center_y': .91}
                            halign: 'right'
                            active: True
                            on_active:
                                trig_opp_adj_deg_checkbox.active = False 
                        MDCheckbox:
                            id: trig_opp_adj_deg_checkbox
                            size_hint: None, None
                            size: dp(40), dp(40)
                            pos_hint: {'center_x': .4, 'center_y': .91}
                            halign: 'right'
                            active: False
                            on_active:
                                trig_opp_adj_rad_checkbox.active = False
                    MDLabel: 
                        text: 'Adjacent'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: trigonometrical_ratios_opposite_which_adj_adjacent
                        hint_text: 'enter adjacent here'
                        helper_text: '= adjacent'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Angle'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: trigonometrical_ratios_opposite_which_adj_angle
                        hint_text: 'enter angle here'
                        helper_text: '= angle'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_trigonometrical_ratios_opposite_which_adj()
                        Widget:
                    TextInput:
                        id: trigonometrical_ratios_opposite_which_adj_text_input    
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
                    Widget:
            Screen:
                name: 'trigonometrical_ratios_hypotenuse'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Which do you have the value for'
                        OneLineListItem:
                            text: 'Opposite'
                            on_release: 
                                screen_manager.current = 'trigonometrical_ratios_hypotenuse_which_opp'
                        OneLineListItem:
                            text: 'Adjacent'
                            on_release:
                                screen_manager.current = 'trigonometrical_ratios_hypotenuse_which_adj'
            Screen:
                name: 'trigonometrical_ratios_hypotenuse_which_opp'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Hypotenuse(Trig.ratios)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel:
                        text: 'RAD   DEG'
                        halign: 'right'
                    BoxLayout:
                        orientation: 'horizontal'
                        Widget:
                        Widget:
                        MDCheckbox:
                            id: trig_hyp_opp_rad_checkbox
                            size_hint: None, None
                            size: dp(40), dp(40)
                            pos_hint: {'center_x': .4, 'center_y': .91}
                            halign: 'right'
                            active: True
                            on_active:
                                trig_hyp_opp_deg_checkbox.active = False 
                        MDCheckbox:
                            id: trig_hyp_opp_deg_checkbox
                            size_hint: None, None
                            size: dp(40), dp(40)
                            pos_hint: {'center_x': .4, 'center_y': .91}
                            halign: 'right'
                            active: False
                            on_active:
                                trig_hyp_opp_rad_checkbox.active = False
                    MDLabel: 
                        text: 'Opposite'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: trigonometrical_ratios_hypotenuse_which_opp_opposite
                        hint_text: 'enter opposite here'
                        helper_text: '= opposite'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Angle'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: trigonometrical_ratios_hypotenuse_which_opp_angle
                        hint_text: 'enter angle here'
                        helper_text: '= angle'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_trigonometrical_ratios_hypotenuse_which_opp()
                        Widget:
                    TextInput:
                        id: trigonometrical_ratios_hypotenuse_which_opp_text_input    
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
                    Widget:
            Screen:
                name: 'trigonometrical_ratios_hypotenuse_which_adj'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Hypotenuse(Trig.ratios)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel:
                        text: 'RAD   DEG'
                        halign: 'right'
                    BoxLayout:
                        orientation: 'horizontal'
                        Widget:
                        Widget:
                        MDCheckbox:
                            id: trig_hyp_adj_rad_checkbox
                            size_hint: None, None
                            size: dp(40), dp(40)
                            pos_hint: {'center_x': .4, 'center_y': .91}
                            halign: 'right'
                            active: True
                            on_active:
                                trig_hyp_adj_deg_checkbox.active = False 
                        MDCheckbox:
                            id: trig_hyp_adj_deg_checkbox
                            size_hint: None, None
                            size: dp(40), dp(40)
                            pos_hint: {'center_x': .4, 'center_y': .91}
                            halign: 'right'
                            active: False
                            on_active:
                                trig_hyp_adj_rad_checkbox.active = False
                    MDLabel: 
                        text: 'Adjacent'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: trigonometrical_ratios_hypotenuse_which_adj_adjacent
                        hint_text: 'enter adjacent here'
                        helper_text: '= adjacent'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Angle'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: trigonometrical_ratios_hypotenuse_which_adj_angle
                        hint_text: 'enter angle here'
                        helper_text: '= angle'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_trigonometrical_ratios_hypotenuse_which_adj()
                        Widget:
                    TextInput: 
                        id: trigonometrical_ratios_hypotenuse_which_adj_text_input   
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
                    Widget:
            Screen:
                name: 'trigonometrical_ratios_adjacent'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Which do you have the value for'
                        OneLineListItem:
                            text: 'Hypotenuse'
                            on_release: 
                                screen_manager.current = 'trigonometrical_ratios_adjacent_which_hyp'
                        OneLineListItem:
                            text: 'Opposite'
                            on_release:
                                screen_manager.current = 'trigonometrical_ratios_adjacent_which_opp'
            Screen:
                name: 'trigonometrical_ratios_adjacent_which_hyp'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Adjacent(Trig.ratios)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel:
                        text: 'RAD   DEG'
                        halign: 'right'
                    BoxLayout:
                        orientation: 'horizontal'
                        Widget:
                        Widget:
                        MDCheckbox:
                            id: trig_adj_hyp_rad_checkbox
                            size_hint: None, None
                            size: dp(40), dp(40)
                            pos_hint: {'center_x': .4, 'center_y': .91}
                            halign: 'right'
                            active: True
                            on_active:
                                trig_adj_hyp_deg_checkbox.active = False 
                        MDCheckbox:
                            id: trig_adj_hyp_deg_checkbox
                            size_hint: None, None
                            size: dp(40), dp(40)
                            pos_hint: {'center_x': .4, 'center_y': .91}
                            halign: 'right'
                            active: False
                            on_active:
                                trig_adj_hyp_rad_checkbox.active = False
                    MDLabel: 
                        text: 'Hypotenuse'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: trigonometrical_ratios_adjacent_which_hyp_hypotenuse
                        hint_text: 'enter hypotenuse here'
                        helper_text: '= hypotenuse'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Angle'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: trigonometrical_ratios_adjacent_which_hyp_angle
                        hint_text: 'enter angle here'
                        helper_text: '= angle'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_trigonometrical_ratios_adjacent_which_hyp()
                        Widget:
                    TextInput:
                        id: trigonometrical_ratios_adjacent_which_hyp_text_input    
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
                    Widget:
            Screen:
                name: 'trigonometrical_ratios_adjacent_which_opp'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Adjacent(Trig.ratios)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel:
                        text: 'RAD   DEG'
                        halign: 'right'
                    BoxLayout:
                        orientation: 'horizontal'
                        Widget:
                        Widget:
                        MDCheckbox:
                            id: trig_adj_opp_rad_checkbox
                            size_hint: None, None
                            size: dp(40), dp(40)
                            pos_hint: {'center_x': .4, 'center_y': .91}
                            halign: 'right'
                            active: True
                            on_active:
                                trig_adj_opp_deg_checkbox.active = False 
                        MDCheckbox:
                            id: trig_adj_opp_deg_checkbox
                            size_hint: None, None
                            size: dp(40), dp(40)
                            pos_hint: {'center_x': .4, 'center_y': .91}
                            halign: 'right'
                            active: False
                            on_active:
                                trig_adj_opp_rad_checkbox.active = False
                    MDLabel: 
                        text: 'Opposite'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: trigonometrical_ratios_adjacent_which_opp_opposite
                        hint_text: 'enter opposite here'
                        helper_text: '= opposite'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Angle'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: trigonometrical_ratios_adjacent_which_opp_angle
                        hint_text: 'enter angle here'
                        helper_text: '= angle'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_trigonometrical_ratios_adjacent_which_opp()
                        Widget:
                    TextInput:
                        id: trigonometrical_ratios_adjacent_which_opp_text_input    
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
                    Widget:
            Screen:
                name: 'statistics'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Mean'
                            on_release:
                                screen_manager.current = 'Mean'
                        OneLineListItem:
                            text: 'Median'
                            on_release:
                                screen_manager.current = 'Median'
                        OneLineListItem:
                            text: 'Mode'
                            on_release:
                                screen_manager.current = 'Mode'
            Screen:
                name: 'percentage_loss_and_profit'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Percentage Profit'
                            on_release:
                                screen_manager.current = 'percentage_profit'
                        OneLineListItem:
                            text: 'Percentage Loss'
                            on_release:
                                screen_manager.current = 'percentage_loss'
            Screen:
                name: 'perimeter_rectangle'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Perimeter(Rectangle)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Length'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: peri_rect_length
                        hint_text: 'enter length here'
                        helper_text: '= Length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Breath'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: peri_rect_breath
                        hint_text: 'enter breath here'
                        helper_text: '= Breath'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_perimeter_rectangle()
                        Widget:
                    Widget:
                    TextInput:    
                        id: peri_rect_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'perimeter_square'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Perimeter(Square)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Length'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: peri_square_length
                        hint_text: 'enter length here'
                        helper_text: '= Length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_perimeter_square()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: peri_square_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'perimeter_triangle'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Perimeter(Triangle)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'A'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: peri_triangle_a
                        hint_text: 'enter side A here'
                        helper_text: '= A'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'B'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: peri_triangle_b
                        hint_text: 'enter side B here'
                        helper_text: '= B'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'C'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: peri_triangle_c
                        hint_text: 'enter side C here'
                        helper_text: '= C'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_perimeter_triangle()
                        Widget:
                    Widget:
                    TextInput:
                        id: peri_triangle_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'perimeter_circle'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'using Diameter'
                            on_release:
                                screen_manager.current = 'using Diameter'
                        OneLineListItem:
                            text: 'using Radius'
                            on_release:
                                screen_manager.current = 'using Radius'
            Screen:
                name: 'using Diameter'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Perimeter(Circle)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Diameter'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: peri_circle_diameter
                        hint_text: 'enter diameter here'
                        helper_text: '= Length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_perimeter_circle_using_diameter()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: perimeter_circle_using_diameter_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'using Radius'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Perimeter(Circle)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Radius'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: peri_circle_radius
                        hint_text: 'enter radius here'
                        helper_text: '= Radius'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_perimeter_circle_using_radius()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: perimeter_circle_using_radius_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'perimeter_parallelogram'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Perimeter(Parallelogram)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Length'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: peri_para_length
                        hint_text: 'enter length here'
                        helper_text: '= Length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Width'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: peri_para_width
                        hint_text: 'enter width here'
                        helper_text: '= Width'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_perimeter_parallelogram()
                        Widget:
                    Widget:
                    TextInput:
                        id: perimeter_parallelogram_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'perimeter_trapezium'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Regular Trapezium'
                            on_release:
                                screen_manager.current = 'regular trapezium'
                        OneLineListItem:
                            text: 'Isosceles Trapezium'
                            on_release:
                                screen_manager.current = 'isosceles trapezium'
            Screen:
                name: 'regular trapezium'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Perimeter(Trapezium)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Top Length'
                        halign: 'left'
                        font_size: 15
                    MDTextField: 
                        id: peri_reg_trap_top_length
                        hint_text: 'enter top length here'
                        helper_text: '= top length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Bottom Length'
                        halign: 'left'
                        font_size: 15
                    MDTextField: 
                        id: peri_reg_trap_bottom_length
                        hint_text: 'enter bottom length here'
                        helper_text: '= bottom length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Left Side Length'
                        halign: 'left'
                        font_size: 15
                    MDTextField: 
                        id: peri_reg_trap_left_length
                        hint_text: 'enter left side length here'
                        helper_text: '= left side length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Right Side Length'
                        halign: 'left'
                        font_size: 15
                    MDTextField: 
                        id: peri_reg_trap_right_length
                        hint_text: 'enter right side length here'
                        helper_text: '= right side length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_perimeter_regular_trapezium()
                        Widget:
                    TextInput:
                        id: peri_regular_trapezium_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'isosceles trapezium'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Perimeter(Trapezium)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Top Length'
                        halign: 'left'
                        font_size: 15
                    MDTextField: 
                        id: peri_iso_trap_top_length
                        hint_text: 'enter top length here'
                        helper_text: '= top length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Bottom Length'
                        halign: 'left'
                        font_size: 15
                    MDTextField: 
                        id: peri_iso_trap_bottom_length
                        hint_text: 'enter bottom length here'
                        helper_text: '= bottom length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Side Length'
                        halign: 'left'
                        font_size: 15
                    MDTextField: 
                        id: peri_iso_trap_side_length
                        hint_text: 'enter side length here'
                        helper_text: '= side length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_perimeter_isosceles_trapezium()
                        Widget:
                    TextInput:
                        id: perimeter_isosceles_trapezium_text_input 
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'perimeter_arc'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Perimeter(Arc)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Radius'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: peri_arc_radius
                        hint_text: 'enter radius here'
                        helper_text: '= Radius'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Angle'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: peri_arc_angle
                        hint_text: 'enter the angle here'
                        helper_text: '= Angle'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_perimeter_arc()
                        Widget:
                    Widget:
                    TextInput:
                        id: perimeter_arc_text_input 
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'area_rectangle'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Area(Rectangle)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Length'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: area_rect_length
                        hint_text: 'enter length here'
                        helper_text: '= Length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Breath'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: area_rect_breath
                        hint_text: 'enter breath here'
                        helper_text: '= Breath'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_area_rectangle()
                        Widget:
                    Widget:
                    TextInput:
                        id: area_rectangle_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'area_square'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Area(Square)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Length'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: area_square_length
                        hint_text: 'enter length here'
                        helper_text: '= Length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_area_square()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: area_square_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'area_triangle'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Area(Triangle)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Height'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: area_tri_height
                        hint_text: 'enter height here'
                        helper_text: '= Height'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Base'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: area_tri_base
                        hint_text: 'enter the angle here'
                        helper_text: '= Base'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_area_triangle()
                        Widget:
                    Widget:
                    TextInput:
                        id: area_triangle_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'area_circle'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'using Diameter'
                            on_release:
                                screen_manager.current = 'using Diameter(Area)'
                        OneLineListItem:
                            text: 'using Radius'
                            on_release:
                                screen_manager.current = 'using Radius(Area)'
            Screen:
                name: 'using Diameter(Area)'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Area(Circle)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Diameter'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: area_circle_diameter
                        hint_text: 'enter diameter here'
                        helper_text: '= diameter'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_area_circle_using_diameter()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: area_circle_using_diameter_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'using Radius(Area)'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Area(Circle)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Radius'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: area_circle_radius
                        hint_text: 'enter radius here'
                        helper_text: '= radius'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_area_circle_using_radius()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: area_circle_using_radius_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'area_parallelogram'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Area(Parallelogram)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Height'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: area_para_height
                        hint_text: 'enter height here'
                        helper_text: '= Height'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Base'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: area_para_base
                        hint_text: 'enter the angle here'
                        helper_text: '= Base'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_area_parallelogram()
                        Widget:
                    Widget:
                    TextInput:
                        id: area_parallelogram_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'area_trapezium'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Area(Trapezium)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'A'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: area_trapezium_a
                        hint_text: 'enter one of the parallel side'
                        helper_text: '= A'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'B'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: area_trapezium_b
                        hint_text: 'enter the other parallel side'
                        helper_text: '= B'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'H'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: area_trapezium_h
                        hint_text: 'enter height'
                        helper_text: '= height'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_area_trapezium()
                        Widget:
                    TextInput:
                        id: area_trapezium_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'area_sector'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Area(Sector)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Radius'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: area_sec_radius
                        hint_text: 'enter height here'
                        helper_text: '= Height'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Angle'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: area_sec_angle
                        hint_text: 'enter the angle here'
                        helper_text: '= angle'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_area_sector()
                        Widget:
                    Widget:
                    TextInput:
                        id: area_sector_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'area_rhombus'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Area(Rhombus)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Diagonal'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: area_rho_d
                        hint_text: 'enter one of the diagonals here'
                        helper_text: '= Diagonal'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Other Diagonal'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: area_rho_d2
                        hint_text: 'enter the other diagonal here'
                        helper_text: '= Diagonal(2)'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_area_rhombus()
                        Widget:
                    Widget:
                    TextInput:
                        id: area_rhombus_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'volume_cube'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Volume(Cube)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Length'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: volume_cube_length
                        hint_text: 'enter length here'
                        helper_text: '= Length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_volume_cube()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: volume_cube_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'volume_cuboid'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Volume(Cuboid)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Length'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: volume_cuboid_l
                        hint_text: 'enter one of the parallel side'
                        helper_text: '= length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Breath'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: volume_cuboid_b
                        hint_text: 'enter the other parallel side'
                        helper_text: '= breath'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Height'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: volume_cuboid_h
                        hint_text: 'enter height'
                        helper_text: '= height'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_volume_cuboid()
                        Widget:
                    TextInput:
                        id: volume_cuboid_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'volume_cylinder'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Volume(Cylinder)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Radius'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: volume_cylinder_radius
                        hint_text: 'enter the radius here'
                        helper_text: '= Radius'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Height'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: volume_cylinder_height
                        hint_text: 'enter the height here'
                        helper_text: '= height'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_volume_cylinder()
                        Widget:
                    Widget:
                    TextInput:
                        id: volume_cylinder_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'volume_cone'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Volume(Cone)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Radius'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: volume_cone_radius
                        hint_text: 'enter the radius here'
                        helper_text: '= Radius'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Height'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: volume_cone_height
                        hint_text: 'enter the height here'
                        helper_text: '= height'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_volume_cone()
                        Widget:
                    Widget:
                    TextInput:
                        id: volume_cone_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'volume_square_based_pyramid'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Volume(Square Based Pyramid)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Base Area'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: volume_square_based_pyramid_base
                        hint_text: 'enter the base area here'
                        helper_text: '= base area'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Height'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: volume_square_based_pyramid_height
                        hint_text: 'enter the height here'
                        helper_text: '= height'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_volume_square_based_pyramid()
                        Widget:
                    Widget:
                    TextInput:
                        id: volume_square_based_pyramid_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'volume_sphere'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Volume(Sphere)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Radius'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: volume_sphere_radius
                        hint_text: 'enter radius here'
                        helper_text: '= Radius'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_volume_sphere()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: volume_sphere_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25    
            Screen:
                name: 'surface_area_cube'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Surface Area(Cube)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Length'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: surface_area_cube_length
                        hint_text: 'enter length here'
                        helper_text: '= Length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_surface_area_cube()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: surface_area_cube_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'surface_area_cuboid'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Surface Area(Cuboid)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Length'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: surface_area_cuboid_length
                        hint_text: 'enter the length here'
                        helper_text: '= length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Breath'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: surface_area_cuboid_breath
                        hint_text: 'enter the breath here'
                        helper_text: '= breath'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Height'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: surface_area_cuboid_height
                        hint_text: 'enter the height here'
                        helper_text: '= height'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_surface_area_cuboid()
                        Widget:
                    TextInput:
                        id: surface_area_cuboid_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'surface_area_cylinder'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Curved Surface Area'
                            on_release:
                                screen_manager.current = 'curved_surface_area_cylinder'
                        OneLineListItem:
                            text: 'Total Surface Area'
                            on_release:
                                screen_manager.current = 'total_surface_area_cylinder'
            Screen:
                name: 'curved_surface_area_cylinder'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Surface Area(Cylinder)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Radius'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: curved_surface_area_cylinder_radius
                        hint_text: 'enter the radius here'
                        helper_text: '= Radius'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Height'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: curved_surface_area_cylinder_height
                        hint_text: 'enter the height here'
                        helper_text: '= height'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_curved_surface_area_cylinder()
                        Widget:
                    Widget:
                    TextInput:
                        id: curved_surface_area_cylinder_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'total_surface_area_cylinder'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Surface Area(Cylinder)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Radius'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: total_surface_area_cylinder_radius
                        hint_text: 'enter the radius here'
                        helper_text: '= Radius'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Height'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: total_surface_area_cylinder_height
                        hint_text: 'enter the height here'
                        helper_text: '= height'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_total_surface_area_cylinder()
                        Widget:
                    Widget:
                    TextInput:
                        id: total_surface_area_cylinder_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'surface_area_sphere'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Surface Area(Sphere)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Radius'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: surface_area_sphere_radius
                        hint_text: 'enter radius here'
                        helper_text: '= Radius'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_surface_area_sphere()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: surface_area_sphere_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'surface_area_cone'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Curved Surface Area'
                            on_release:
                                screen_manager.current = 'curved_surface_area_cone'
                        OneLineListItem:
                            text: 'Total Surface Area'
                            on_release:
                                screen_manager.current = 'total_surface_area_cone'
            Screen:
                name: 'curved_surface_area_cone'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Surface Area(Cone)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Radius'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: curved_surface_area_cone_radius
                        hint_text: 'enter the radius here'
                        helper_text: '= Radius'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Length'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: curved_surface_area_cone_length
                        hint_text: 'enter the length here'
                        helper_text: '= length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_curved_surface_area_cone()
                        Widget:
                    Widget:
                    TextInput:
                        id: curved_surface_area_cone_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'total_surface_area_cone'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Surface Area(Cone)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Radius'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: total_surface_area_cone_radius
                        hint_text: 'enter the radius here'
                        helper_text: '= Radius'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Length'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: total_surface_area_cone_length
                        hint_text: 'enter the length here'
                        helper_text: '= length'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_total_surface_area_cone()
                        Widget:
                    Widget:
                    TextInput:
                        id: total_surface_area_cone_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'nth term(Linear Sequence)'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Linear Sequence'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'First Term'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: nth_term_linear_sequence_a
                        hint_text: 'enter the first term'
                        helper_text: '= first term'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Common Difference'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: nth_term_linear_sequence_d
                        hint_text: 'enter the common difference'
                        helper_text: '= common difference'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Nth term'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: nth_term_linear_sequence_n
                        hint_text: 'enter the nth term'
                        helper_text: '= nth term'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_nth_term_linear_sequence()
                        Widget:
                    TextInput:
                        id: nth_term_linear_sequence_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'arithmetic_mean'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Arithmetic Mean'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'a'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: arithmetic_mean_a
                        hint_text: 'enter first or previous number'
                        helper_text: '= a'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'c'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: arithmetic_mean_c
                        hint_text: 'enter the third or next number'
                        helper_text: '= c'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_arithmetic_mean()
                        Widget:
                    Widget:
                    TextInput:
                        id: arithmetic_mean_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'Sum of n terms(Linear Sequence)'
                BoxLayout:
                    orientation: 'vertical'
                    BoxLayout:
                        orientation: 'vertical'
                        MDLabel: 
                            text: 'Do you have the first and second term'
                            pos_hint: {'center_x': .5, 'center_y': .94}
                        MDLabel:
                            text: 'Yes   No'
                            pos_hint: {'center_x': .5, 'center_y': .94}
                            halign: 'right'
                        BoxLayout:
                            orientation: 'horizontal'
                            Widget:
                            Widget:
                            Widget:
                            MDCheckbox:
                                size_hint: None, None
                                size: dp(40), dp(40)
                                pos_hint: {'center_x': .4, 'center_y': .91}
                                halign: 'right'
                                active: True
                            MDCheckbox:
                                id: checkbox_last_term
                                size_hint: None, None
                                size: dp(40), dp(40)
                                pos_hint: {'center_x': .3, 'center_y': .91}
                                active: False
                                on_active: 
                                    screen_manager.current = 'show_sum_of_n_terms_linear_sequence_last_term'
                        MDLabel: 
                            text: 'First Term'
                            halign: 'left'
                            font_size: 25
                        MDTextField: 
                            id: show_sum_of_n_terms_linear_sequence_a
                            hint_text: 'enter the first term'
                            helper_text: '= first term'
                            helper_text_mode: 'on_focus'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                            size_hint_x: None
                            width: 150
                        MDLabel: 
                            text: 'Common Difference'
                            halign: 'left'
                            font_size: 25
                        MDTextField: 
                            id: show_sum_of_n_terms_linear_sequence_d
                            hint_text: 'enter the common difference'
                            helper_text: '= common difference'
                            helper_text_mode: 'on_focus'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                            size_hint_x: None
                            width: 150
                        MDLabel: 
                            text: 'nth term'
                            halign: 'left'
                            font_size: 25
                        MDTextField: 
                            id: show_sum_of_n_terms_linear_sequence_n
                            hint_text: 'enter the nth term'
                            helper_text: '= nth term'
                            helper_text_mode: 'on_focus'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                            size_hint_x: None
                            width: 150
                        BoxLayout:
                            Widget:
                            MDIconButton:
                                icon: 'equal'
                                on_release: app.show_sum_of_n_terms_linear_sequence()
                            Widget:
                        TextInput:
                            id: sum_of_n_terms_linear_sequence_text_input
                            multiline: False 
                            readonly:True 
                            halign: 'right' 
                            font_size: 25
            Screen:
                name: 'show_sum_of_n_terms_linear_sequence_last_term'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Linear Sequence'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'First Term'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: show_sum_of_n_terms_linear_sequence_last_term_a
                        hint_text: 'enter the first term here'
                        helper_text: '= first term'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Number of terms'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: show_sum_of_n_terms_linear_sequence_last_term_n
                        hint_text: 'enter numbers of terms'
                        helper_text: '= number of terms'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Last term'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: show_sum_of_n_terms_linear_sequence_last_term_l
                        hint_text: 'enter last term here'
                        helper_text: '= last term'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_sum_of_n_terms_linear_sequence_last_term()
                        Widget:
                    TextInput:
                        id: sum_of_n_terms_linear_sequence_last_term_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'nth term(Geometric Progression)'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Geometric Progression'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'First Term'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: nth_term_geometric_progression_a
                        hint_text: 'enter the first term here'
                        helper_text: '= first term'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Common Ratio'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: nth_term_geometric_progression_r
                        hint_text: 'enter the common ratio here'
                        helper_text: '= common ratio'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Nth term'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: nth_term_geometric_progression_n
                        hint_text: 'enter the nth term here'
                        helper_text: '= nth term'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_nth_term_geometric_progression()
                        Widget:
                    TextInput:
                        id: nth_term_geometric_progression_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'Geometric mean'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Geometric Mean'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'a'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: geometric_mean_a
                        hint_text: 'enter first or previous number'
                        helper_text: '= a'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'c'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: geometric_mean_c
                        hint_text: 'enter third or next number'
                        helper_text: '= c'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_geometric_mean()
                        Widget:
                    TextInput:
                        id: geometric_mean_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'Sum of n terms(Geometric Progression)'
                BoxLayout:
                    orientation: 'vertical'
                    BoxLayout:
                        orientation: 'vertical'
                        MDLabel: 
                            text: 'Is your common ratio = 1, > 1, or < 1'
                            pos_hint: {'center_x': .5, 'center_y': .94}
                        MDLabel:
                            text: '=1   >1    <1    '
                            pos_hint: {'center_x': .5, 'center_y': .94}
                            halign: 'right'
                        BoxLayout:
                            orientation: 'horizontal'
                            Widget:
                            Widget:
                            Widget:
                            MDCheckbox:
                                size_hint: None, None
                                size: dp(40), dp(40)
                                pos_hint: {'center_x': .4, 'center_y': .91}
                                halign: 'right'
                                active: True
                            MDCheckbox:
                                id: checkbox_greater_one
                                size_hint: None, None
                                size: dp(40), dp(40)
                                pos_hint: {'center_x': .3, 'center_y': .91}
                                active: False
                                on_active: 
                                    screen_manager.current = 'sum_of_n_terms_geometric_progression_greater_one'
                            MDCheckbox:
                                id: checkbox_lesser_one
                                size_hint: None, None
                                size: dp(40), dp(40)
                                pos_hint: {'center_x': .3, 'center_y': .91}
                                active: False
                                on_active: 
                                    screen_manager.current = 'sum_of_n_terms_geometric_progression_lesser_one'
                        MDLabel: 
                            text: 'Number of Terms'
                            halign: 'left'
                            font_size: 25
                        MDTextField: 
                            id: show_sum_of_n_terms_geometric_progression_equal_one_number_terms
                            hint_text: 'enter number of terms'
                            helper_text: '= number of terms'
                            helper_text_mode: 'on_focus'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                            size_hint_x: None
                            width: 150
                        MDLabel: 
                            text: 'First term'
                            halign: 'left'
                            font_size: 25
                        MDTextField: 
                            id: show_sum_of_n_terms_geometric_progression_equal_one_first_term
                            hint_text: 'enter first term'
                            helper_text: '= first term'
                            helper_text_mode: 'on_focus'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                            size_hint_x: None
                            width: 150
                        BoxLayout:
                            Widget:
                            MDIconButton:
                                icon: 'equal'
                                on_release: app.show_sum_of_n_terms_geometric_progression_equal_one()
                            Widget:
                        Widget:
                        TextInput:
                            id: sum_of_n_terms_geometric_progression_equal_one_text_input
                            multiline: False 
                            readonly:True 
                            halign: 'right' 
                            font_size: 25
            Screen:
                name: 'sum_of_n_terms_geometric_progression_greater_one'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'sum of n terms(geometric progression)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Number of Terms'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: sum_of_n_terms_geometric_progression_greater_one_number_of_terms
                        hint_text: 'enter number of terms'
                        helper_text: '= number of terms'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'First Term'
                        halign: 'left'
                        font_size: 25
                    MDLabel: 
                        text: 'Common Ratio'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: sum_of_n_terms_geometric_progression_greater_one_common_ratio
                        hint_text: 'enter common ratio'
                        helper_text: '= ratio'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_sum_of_n_terms_geometric_progression_greater_one()
                        Widget:
                    TextInput:
                        id: sum_of_n_terms_geometric_progression_greater_one_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'sum_of_n_terms_geometric_progression_lesser_one'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'sum of n terms(geometric progression)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Number of Terms'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: sum_of_n_terms_geometric_progression_lesser_one_number_of_terms
                        hint_text: 'enter number of terms'
                        helper_text: '= number of terms'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'First Term'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: sum_of_n_terms_geometric_progression_lesser_one_first_term
                        hint_text: 'enter first term here'
                        helper_text: '= first term'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Common Ratio'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: sum_of_n_terms_geometric_progression_lesser_one_common_ratio
                        hint_text: 'enter common ratio'
                        helper_text: '= ratio'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_sum_of_n_terms_geometric_progression_lesser_one()
                        Widget:
                    TextInput:
                        id: sum_of_n_terms_geometric_progression_lesser_one_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'Sum to Infinity'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Sum to Infinity'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'First Term'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: sum_to_infinity_first_term
                        hint_text: 'enter first term here'
                        helper_text: '= first term'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Common Ratio'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: sum_to_infinity_common_ratio
                        hint_text: 'enter common ratio here'
                        helper_text: '= common ratio'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_sum_to_infinity()
                        Widget:
                    Widget:
                    TextInput:
                        id: sum_to_infinity_text_input    
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'Simple Interest'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Simple Interest'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Principal'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: simple_interest_p
                        hint_text: 'enter principal here'
                        helper_text: '= principal'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Rate'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: simple_interest_r
                        hint_text: 'enter rate here'
                        helper_text: '= rate'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Time'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: simple_interest_t
                        hint_text: 'enter time here'
                        helper_text: '= time'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_simple_interest()
                        Widget:
                    TextInput:
                        id: simple_interest_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'Rate'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Simple Interest(Rate)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Interest'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: rate_i
                        hint_text: 'enter interest here'
                        helper_text: '= interest'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Principal'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: rate_p
                        hint_text: 'enter principal here'
                        helper_text: '= principal'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Time'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: rate_t
                        hint_text: 'enter time here'
                        helper_text: '= time'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_rate()
                        Widget:
                    TextInput:
                        id: rate_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'Time'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Simple Interest(Time)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Interest'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: time_i
                        hint_text: 'enter interest here'
                        helper_text: '= interest'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Principal'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: time_p
                        hint_text: 'enter principal here'
                        helper_text: '= principal'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Rate'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: time_r
                        hint_text: 'enter rate here'
                        helper_text: '= rate'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_time()
                        Widget:
                    TextInput:
                        id: time_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'Principal'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Simple Interest(Principal)'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Interest'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: principal_i
                        hint_text: 'enter interest here'
                        helper_text: '= interest'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Time'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: principal_t
                        hint_text: 'enter time here'
                        helper_text: '= time'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Rate'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: principal_r
                        hint_text: 'enter rate here'
                        helper_text: '= rate'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_principal()
                        Widget:
                    TextInput:
                        id: principal_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'linear_equation'
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Linear Equation'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    Widget:
                    MDTextField: 
                        id: linear_equation
                        hint_text: 'enter equation here'
                        helper_text: ''
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'solve'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                            on_release: app.show_linear_equation()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: linear_equation_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 20
            Screen:
                name: 'quadratic_equation'
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Quadratic Equation'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    Widget:
                    MDTextField: 
                        id: quadratic_equation
                        hint_text: 'enter equation here'
                        helper_text: ''
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'solve'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                            on_release: app.show_quadratic_equation()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: quadratic_equation_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 20
            Screen:
                name: 'simultaneous_equation'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Simultaneous Equation'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'First equation'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: simultaneous_equation_first
                        hint_text: 'enter first equation'
                        helper_text: '= first equation'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Second Equation'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: simultaneous_equation_second
                        hint_text: 'enter second equation'
                        helper_text: '= second equation'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_simultaneous_equation()
                        Widget:
                    Widget:
                    TextInput:    
                        id: simultaneous_equation_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'quadratic_equations_from_roots'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Quadratic Equation From Roots'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'First Root'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: quadratic_equations_first
                        hint_text: 'enter first equation'
                        helper_text: '= first equation'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Second Root'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: quadratic_equations_second
                        hint_text: 'enter second equation'
                        helper_text: '= second equation'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_quadratic_equations_from_roots()
                        Widget:
                    Widget:
                    TextInput:
                        id: quadratic_equations_from_roots_text_input    
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'distance'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Distance'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Time'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: distance_time
                        hint_text: 'enter time value '
                        helper_text: '= time'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Speed'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: distance_speed
                        hint_text: 'enter speed value'
                        helper_text: '= speed'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_distance()
                        Widget:
                    TextInput:
                        id: distance_text_input    
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'time'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Time'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Speed'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: time_speed
                        hint_text: 'enter speed value '
                        helper_text: '= speed'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Distance'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: time_distance
                        hint_text: 'enter distance value'
                        helper_text: '= distance'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_time_in_distance()
                        Widget:
                    TextInput:
                        id: time_in_distance_text_input    
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'speed'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Speed'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Distance'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: speed_distance
                        hint_text: 'enter distance value '
                        helper_text: '= distance'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Time'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: speed_time
                        hint_text: 'enter time value'
                        helper_text: '= time'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_speed()
                        Widget:
                    TextInput:
                        id: speed_text_input    
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'Mean'
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Mean'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    Widget:
                    MDTextField: 
                        id: mean
                        hint_text: 'enter numbers here'
                        helper_text: 'enter numbers separated by , e.g 1,2,3'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_mean()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: mean_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 20
            Screen:
                name: 'Median'
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Median'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    Widget:
                    MDTextField: 
                        id: median
                        hint_text: 'enter numbers here'
                        helper_text: 'enter numbers separated by , e.g 1,2,3'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_median()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: median_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 55
            Screen:
                name: 'Mode'
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Mode'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    Widget:
                    MDTextField:
                        id: mode 
                        hint_text: 'enter numbers here'
                        helper_text: 'enter numbers separated by , e.g 1,2,3'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDIconButton:
                            icon: 'equal'
                            on_release: app.show_mode()
                        Widget:
                    Widget:
                    Widget:
                    TextInput:
                        id: mode_text_input
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 55
            Screen:
                name: 'percentage_profit'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Percentage Profit'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Profit'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: percentage_profit_profit
                        hint_text: 'enter profit'
                        helper_text: '= profit'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Cost Price'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: percentage_profit_cost_price
                        hint_text: 'enter cost price'
                        helper_text: '= cost price'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_percentage_profit()
                        Widget:
                    Widget:
                    TextInput:
                        id: percentage_profit_text_input    
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'percentage_loss'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '0dp'
                    MDToolbar:
                        title: 'Percentage Loss'
                        left_action_items: [['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel: 
                        text: 'Loss'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: percentage_loss_loss
                        hint_text: 'enter loss'
                        helper_text: '= loss'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    MDLabel: 
                        text: 'Cost Price'
                        halign: 'left'
                        font_size: 25
                    MDTextField: 
                        id: percentage_loss_cost_price
                        hint_text: 'enter cost price'
                        helper_text: '= cost price'
                        helper_text_mode: 'on_focus'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        size_hint_x: None
                        width: 150
                    BoxLayout:
                        Widget:
                        MDRectangleFlatButton:
                            text: 'Solve'
                            on_release: app.show_percentage_loss()
                        Widget:
                    Widget:
                    TextInput:
                        id: percentage_loss_text_input    
                        multiline: False 
                        readonly:True 
                        halign: 'right' 
                        font_size: 25
            Screen:
                name: 'settings'
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Theme and Color'
                            on_release: app.theme_pick()
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                ScrollView:
                    MDList:
                        TwoLineListItem:
                            text: 'Homepage'
                            on_release: 
                                screen_manager.current = 'screen_one'
                        TwoLineListItem:
                            text: 'Perimeter'
                            on_release: 
                                screen_manager.current = 'perimeter_screen'
                        TwoLineListItem:
                            text: 'Area'
                            on_release:
                                screen_manager.current = 'area_screen'
                        TwoLineListItem:
                            text: 'Volume'
                            on_release:
                                screen_manager.current = 'volume_screen'
                        TwoLineListItem:
                            text: 'Surface Area'
                            on_release:
                                screen_manager.current = 'surface_area'
                        TwoLineListItem:
                            text: 'Series and Sequences'
                            on_release:
                                screen_manager.current = 'series_and_sequences'
                        TwoLineListItem:
                            text: 'Simple Interest'
                            secondary_text: 'Rate,Time,Principal'
                            on_release:
                                screen_manager.current = 'simple_interest'
                        TwoLineListItem:
                            text: 'Compound Interest'
                            on_release:
                                screen_manager.current = 'compound_interest'
                        TwoLineListItem:
                            text: 'Angles'
                            on_release:
                                screen_manager.current = 'angles'
                        TwoLineListItem:
                            text: 'Equations'
                            on_release:
                                screen_manager.current = 'equations'
                        TwoLineListItem:
                            text: 'Modular Arithmetic'
                            on_release:
                                screen_manager.current = 'modular_arithmetic'
                        TwoLineListItem:
                            text: 'Distance,Time and Speed'
                            on_release:
                                screen_manager.current = 'Distance,Time and Speed'
                        TwoLineListItem:
                            text: 'Pythagoras Theorem'
                            on_release:
                                screen_manager.current = 'pythagoras_theorem'
                        TwoLineListItem:
                            text: 'Trigonometrical ratios'
                            secondary_text: 'to find hyp,adj and opp'
                            on_release:
                                screen_manager.current = 'trigonometrical_ratios'
                        TwoLineListItem:
                            text: 'Statistics'
                            secondary_text: 'Mean,Median and Mode'
                            on_release:
                                screen_manager.current = 'statistics'
                        TwoLineListItem:
                            text: 'Percentage loss and profit'
                            on_release:
                                screen_manager.current = 'percentage_loss_and_profit'
                        TwoLineListItem:
                            text: 'Settings'
                            on_release:
                                screen_manager.current = 'settings'
'''


class CalculateAllApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Dark'
        self.title = 'CalculateAll'
        self.icon = 'calculator.png'
        screen = Builder.load_string(screen_helper)
        # screen = Builder.load_file('calculateAll.kv')
        return screen

    def theme_pick(self):
        try:
            self.theme_cls.primary_hue = '500'
            picker = MDThemePicker()
            picker.open()
        except KeyError:
            toast('Avoid changing the colour and theme regularly')
        except:
            toast('Avoid changing the colour and theme regularly')

    def on_button_press(self, button_id):
        if button_id is self.root.ids.plus_sign:
            not_sign_button_text = '+'
            self.root.ids.show.text += not_sign_button_text
        elif button_id is self.root.ids.minus_sign:
            not_sign_button_text = '-'
            self.root.ids.show.text += not_sign_button_text
        elif button_id is self.root.ids.division_sign:
            not_sign_button_text = '/'
            self.root.ids.show.text += not_sign_button_text
        elif button_id is self.root.ids.multiply_sign:
            not_sign_button_text = '*'
            self.root.ids.show.text += not_sign_button_text
        elif button_id is self.root.ids.decimal_point:
            not_sign_button_text = '.'
            self.root.ids.show.text += not_sign_button_text
        elif button_id is self.root.ids.inv:
            not_sign_button_text = 'inv('
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.deg:
            if self.root.ids.deg.text == 'DEG':
                self.root.ids.deg.text = 'RAD'
            elif self.root.ids.deg.text == 'RAD':
                self.root.ids.deg.text = 'DEG'
        elif button_id is self.root.ids.deg_two:
            self.root.ids.deg_two.text = self.root.ids.deg.text
        elif button_id is self.root.ids.percent:
            not_sign_button_text = 'per('
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.sin:
            if self.root.ids.deg.text == 'RAD':
                not_sign_button_text = 'sin('
                self.root.ids.show.text += not_sign_button_text
            elif self.root.ids.deg.text == 'DEG':
                not_sign_button_text = 'sin('
                self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.cos:
            not_sign_button_text = 'cos('
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.tan:
            not_sign_button_text = 'tan('
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.In:
            not_sign_button_text = 'ln('
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.log:
            not_sign_button_text = 'log10('
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.combination:
            not_sign_button_text = 'fact('
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.pi:
            not_sign_button_text = 'pi'
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.e:
            not_sign_button_text = 'e'
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.to_power:
            not_sign_button_text = '**'
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.front_bracket:
            not_sign_button_text = '('
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.end_bracket:
            not_sign_button_text = ')'
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.sq_root:
            not_sign_button_text = 'sqrt('
            self.root.ids.show.text += not_sign_button_text
            self.root.ids_screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.sin_inv:
            not_sign_button_text = 'asin('
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.cos_inv:
            not_sign_button_text = 'acos('
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.tan_inv:
            not_sign_button_text = 'atan('
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.e_to_power_x:
            not_sign_button_text = 'exp('
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.anti_log:
            not_sign_button_text = '10**('
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        elif button_id is self.root.ids.squared:
            not_sign_button_text = '**2'
            self.root.ids.show.text += not_sign_button_text
            self.root.ids.screen_manager.current = self.root.ids.screen_one.name
        else:
            button_text = button_id.text
            self.root.ids.show.text += button_text

    def clear_screen(self):
        self.root.ids.show.text = ''

    def on_solution(self):
        try:
            operators = ['/', '*']
            screen_text = self.root.ids.show.text
            if screen_text == '':
                return
            elif screen_text[0] in operators:
                toast('The first is a operator')
            else:
                if self.root.ids.deg.text == 'RAD':
                    screen = self.root.ids.show.text.replace('sin', 'sin_r').replace('cos', 'cos_r'). \
                        replace('tan', 'tan_r').replace('asin', 'asin_r').replace('acos', 'acos_r'). \
                        replace('atan', 'atan_r')
                    solution = str(eval(screen))
                    self.root.ids.show.text = solution
                else:
                    solution = str(eval(self.root.ids.show.text))
                    self.root.ids.show.text = solution
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        except SyntaxError:
            toast('Don’t put operators beside each other,place your brackets correctly')
        except NameError:
            toast('incorrect syntax,place your brackets correctly')
        except TypeError:
            toast('incorrect syntax,place your brackets correctly')

    def show_perimeter_rectangle(self):
        try:
            length = float(self.root.ids.peri_rect_length.text)
            breath = float(self.root.ids.peri_rect_breath.text)
            perimeter = 2 * (length + breath)
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.peri_rect_text_input.text = str(perimeter)

    def show_perimeter_square(self):
        try:
            length = float(self.root.ids.peri_square_length.text)
            perimeter = 4 * length
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.peri_square_text_input.text = str(perimeter)

    def show_perimeter_triangle(self):
        try:
            a = float(self.root.ids.peri_triangle_a.text)
            b = float(self.root.ids.peri_triangle_b.text)
            c = float(self.root.ids.peri_triangle_c.text)
            perimeter = a + b + c
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.peri_triangle_text_input.text = str(perimeter)

    def show_perimeter_circle_using_diameter(self):
        try:
            diameter = float(self.root.ids.peri_circle_diameter.text)
            perimeter = float(pi * diameter)
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.perimeter_circle_using_diameter_text_input.text = str(perimeter)

    def show_perimeter_circle_using_radius(self):
        try:
            radius = float(self.root.ids.peri_circle_radius.text)
            perimeter = float(2 * pi * radius)
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.perimeter_circle_using_radius_text_input.text = str(perimeter)

    def show_perimeter_parallelogram(self):
        try:
            length = float(self.root.ids.peri_para_length.text)
            width = float(self.root.ids.peri_para_width.text)
            perimeter = float(2 * (length + width))
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.perimeter_parallelogram_text_input.text = str(perimeter)

    def show_perimeter_regular_trapezium(self):
        try:
            top = float(self.root.ids.peri_reg_trap_top_length.text)
            bottom = float(self.root.ids.peri_reg_trap_bottom_length.text)
            left_side_length = float(self.root.ids.peri_reg_trap_left_length.text)
            right_side_length = float(self.root.ids.peri_reg_trap_right_length.text)
            perimeter = float(top + bottom + left_side_length + right_side_length)
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.peri_regular_trapezium_text_input.text = str(perimeter)

    def show_perimeter_isosceles_trapezium(self):
        try:
            top = float(self.root.ids.peri_iso_trap_top_length.text)
            bottom = float(self.root.ids.peri_iso_trap_bottom_length.text)
            side_length = float(self.root.ids.peri_iso_trap_side_length.text)
            perimeter = float((2 * side_length) + top + bottom)
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.perimeter_isosceles_trapezium_text_input.text = str(perimeter)

    def show_perimeter_arc(self):
        try:
            r = float(self.root.ids.peri_arc_radius.text)
            angle = float(self.root.ids.peri_arc_angle.text)
            length_of_arc = float(angle / 360 * 2 * pi * r)
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.perimeter_arc_text_input.text = str(length_of_arc)

    def show_area_rectangle(self):
        try:
            length = float(self.root.ids.area_rect_length.text)
            breath = float(self.root.ids.area_rect_breath.text)
            area = length * breath
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.area_rectangle_text_input.text = str(area)

    def show_area_square(self):
        try:
            length = float(self.root.ids.area_square_length.text)
            area = length * length
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.area_square_text_input.text = str(area)

    def show_area_triangle(self):
        try:
            height = float(self.root.ids.area_tri_height.text)
            base = float(self.root.ids.area_tri_base.text)
            area = 0.5 * (height * base)
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.area_triangle_text_input.text = str(area)

    def show_area_circle_using_diameter(self):
        try:
            diameter = float(self.root.ids.area_circle_diameter.text)
            area = float(pi * (diameter / 2) ** 2)
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.area_circle_using_diameter_text_input.text = str(area)

    def show_area_circle_using_radius(self):
        try:
            radius = float(self.root.ids.area_circle_radius.text)
            area = float(pi * (radius ** 2))
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.area_circle_using_radius_text_input.text = str(area)

    def show_area_parallelogram(self):
        try:
            base = float(self.root.ids.area_para_height.text)
            height = float(self.root.ids.area_para_base.text)
            area = float(base * height)
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.area_parallelogram_text_input.text = str(area)

    def show_area_trapezium(self):
        try:
            a = float(self.root.ids.area_trapezium_a.text)
            b = float(self.root.ids.area_trapezium_b.text)
            h = float(self.root.ids.area_trapezium_h.text)
            area = float(0.5 * (a + b) * h)
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.area_trapezium_text_input.text = str(area)

    def show_area_sector(self):
        try:
            r = float(self.root.ids.area_sec_radius.text)
            angle = float(self.root.ids.area_sec_angle.text)
            area = float(angle / 360 * pi * r ** 2)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.area_sector_text_input.text = str(area)

    def show_area_rhombus(self):
        try:
            d = float(self.root.ids.area_rho_d.text)
            d1 = float(self.root.ids.area_rho_d2.text)
            area = float(0.5 * d * d1)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.area_rhombus_text_input.text = str(area)

    def show_volume_cube(self):
        try:
            length = float(self.root.ids.volume_cube_length.text)
            volume = float(length ** 3)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.volume_cube_text_input.text = str(volume)

    def show_volume_cuboid(self):
        try:
            length = float(self.root.ids.volume_cuboid_l.text)
            b = float(self.root.ids.volume_cuboid_b.text)
            h = float(self.root.ids.volume_cuboid_h.text)
            volume = float(length * b * h)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.volume_cuboid_text_input.text = str(volume)

    def show_volume_cylinder(self):
        try:
            r = float(self.root.ids.volume_cylinder_radius.text)
            h = float(self.root.ids.volume_cylinder_height.text)
            volume = float(pi * (r ** 2) * h)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.volume_cylinder_text_input.text = str(volume)

    def show_volume_cone(self):
        try:
            r = float(self.root.ids.volume_cone_radius.text)
            h = float(self.root.ids.volume_cone_height.text)
            volume = float(1 / 3 * pi * r ** 2 * h)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.volume_cone_text_input.text = str(volume)

    def show_volume_square_based_pyramid(self):
        try:
            b = float(self.root.ids.volume_square_based_pyramid_base.text)
            h = float(self.root.ids.volume_square_based_pyramid_height.text)
            volume = float(1 / 3 * b * h)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.volume_square_based_pyramid_text_input.text = str(volume)

    def show_volume_sphere(self):
        try:
            r = float(self.root.ids.volume_sphere_radius.text)
            volume = float(4 / 3 * pi * r ** 3)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.volume_sphere_text_input.text = str(volume)

    def show_surface_area_cube(self):
        try:
            length = float(self.root.ids.surface_area_cube_length.text)
            surface_area = float(6 * (length ** 2))
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.surface_area_cube_text_input.text = str(surface_area)

    def show_surface_area_cuboid(self):
        try:
            length = float(self.root.ids.surface_area_cuboid_length.text)
            b = float(self.root.ids.surface_area_cuboid_breath.text)
            h = float(self.root.ids.surface_area_cuboid_height.text)
            surface_area = float((length * b) + (length * h) + (b * h))
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.surface_area_cuboid_text_input.text = str(surface_area)

    def show_curved_surface_area_cylinder(self):
        try:
            r = float(self.root.ids.curved_surface_area_cylinder_radius.text)
            h = float(self.root.ids.curved_surface_area_cylinder_height.text)
            surface_area = float(2 * pi * r * h)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.curved_surface_area_cylinder_text_input.text = str(surface_area)

    def show_total_surface_area_cylinder(self):
        try:
            r = float(self.root.ids.total_surface_area_cylinder_radius.text)
            h = float(self.root.ids.total_surface_area_cylinder_height.text)
            tot_sur_area = float((2 * pi * r * h) + (2 * pi * r ** 2))
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.total_surface_area_cylinder_text_input.text = str(tot_sur_area)

    def show_surface_area_sphere(self):
        try:
            r = float(self.root.ids.surface_area_sphere_radius.text)
            surf_ar = float(4 * pi * r ** 3)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.surface_area_sphere_text_input.text = str(surf_ar)

    def show_curved_surface_area_cone(self):
        try:
            r = float(self.root.ids.curved_surface_area_cone_radius.text)
            length = float(self.root.ids.curved_surface_area_cone_length.text)
            surface_area = float(pi * r * length)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.curved_surface_area_cone_text_input.text = str(surface_area)

    def show_total_surface_area_cone(self):
        try:
            r = float(self.root.ids.total_surface_area_cone_radius.text)
            length = float(self.root.ids.total_surface_area_cone_length.text)
            tot_surf_ar = float((pi * r * length) + (pi * r ** 2))
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.total_surface_area_cone_text_input.text = str(tot_surf_ar)

    def show_nth_term_linear_sequence(self):
        try:
            a = float(self.root.ids.nth_term_linear_sequence_a.text)
            d = float(self.root.ids.nth_term_linear_sequence_d.text)
            n = int(self.root.ids.nth_term_linear_sequence_n.text)
            tn = a + (n - 1) * d
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.nth_term_linear_sequence_text_input.text = 'The ' + str(n) + 'th term is ' + str(tn)

    def show_arithmetic_mean(self):
        try:
            a = float(self.root.ids.arithmetic_mean_a.text)
            c = float(self.root.ids.arithmetic_mean_c.text)
            b = (a + c) / 2
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.arithmetic_mean_text_input.text = str(b)

    def show_sum_of_n_terms_linear_sequence(self):
        try:
            a = float(self.root.ids.show_sum_of_n_terms_linear_sequence_a.text)
            d = float(self.root.ids.show_sum_of_n_terms_linear_sequence_d.text)
            n = float(self.root.ids.show_sum_of_n_terms_linear_sequence_n.text)
            sn = (n / 2) * (2 * a + (n - 1) * d)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.sum_of_n_terms_linear_sequence_text_input.text = str(sn)

    def show_sum_of_n_terms_linear_sequence_last_term(self):
        try:
            a = float(self.root.ids.show_sum_of_n_terms_linear_sequence_last_term_a.text)
            n = float(self.root.ids.show_sum_of_n_terms_linear_sequence_last_term_n.text)
            last = float(self.root.ids.show_sum_of_n_terms_linear_sequence_last_term_l.text)
            sn = (n / 2) * (a + last)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.sum_of_n_terms_linear_sequence_last_term_text_input.text = str(sn)

    def show_nth_term_geometric_progression(self):
        try:
            a = float(self.root.ids.nth_term_geometric_progression_a.text)
            r = float(self.root.ids.nth_term_geometric_progression_r.text)
            n = int(self.root.ids.nth_term_geometric_progression_n.text)
            Tn = a * r ** (n - 1)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.nth_term_geometric_progression_text_input.text = str(Tn)

    def show_geometric_mean(self):
        try:
            a = float(self.root.ids.geometric_mean_a.text)
            c = float(self.root.ids.geometric_mean_c.text)
            b = (a * c) ** (1 / 2)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.geometric_mean_text_input.text = str(b)

    def show_sum_of_n_terms_geometric_progression_equal_one(self):
        try:
            n = int(self.root.ids.show_sum_of_n_terms_geometric_progression_equal_one_number_terms.text)
            a = float(self.root.ids.show_sum_of_n_terms_geometric_progression_equal_one_first_term.text)
            sn = n * a
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.sum_of_n_terms_geometric_progression_equal_one_text_input.text = str(sn)

    def show_sum_of_n_terms_geometric_progression_greater_one(self):
        try:
            n = int(self.root.ids.sum_of_n_terms_geometric_progression_greater_one_number_of_terms.text)
            a = float(self.root.ids.sum_of_n_terms_geometric_progression_greater_one_first_term.text)
            r = float(self.root.ids.sum_of_n_terms_geometric_progression_greater_one_common_ratio.text)
            sn = (a * ((r ** n) - 1) / (r - 1))
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.sum_of_n_terms_geometric_progression_greater_one_text_input.text = str(sn)

    def show_sum_of_n_terms_geometric_progression_lesser_one(self):
        try:
            n = int(self.root.ids.sum_of_n_terms_geometric_progression_lesser_one_number_of_terms.text)
            a = float(self.root.ids.sum_of_n_terms_geometric_progression_lesser_one_first_term.text)
            r = float(self.root.ids.sum_of_n_terms_geometric_progression_lesser_one_common_ratio.text)
            Sn = (a * (1 - (r ** n))) / (1 - r)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.sum_of_n_terms_geometric_progression_lesser_one_text_input.text = str(Sn)

    def show_sum_to_infinity(self):
        try:
            a = float(self.root.ids.sum_to_infinity_first_term.text)
            r = float(self.root.ids.sum_to_infinity_common_ratio.text)
            sum_to_infinity = a / (1 - r)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.sum_to_infinity_text_input.text = str(sum_to_infinity)

    def show_simple_interest(self):
        try:
            p = float(self.root.ids.simple_interest_p.text)
            r = float(self.root.ids.simple_interest_r.text)
            t = float(self.root.ids.simple_interest_t.text)
            i = float((p * r * t) / 100)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.simple_interest_text_input.text = str(i)

    def show_rate(self):
        try:
            i = float(self.root.ids.rate_i.text)
            p = float(self.root.ids.rate_p.text)
            t = float(self.root.ids.rate_t.text)
            r = float(100 * i / p * t)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.rate_text_input.text = str(r)

    def show_time(self):
        try:
            i = float(self.root.ids.time_i.text)
            p = float(self.root.ids.time_p.text)
            r = float(self.root.ids.time_r.text)
            t = float((100 * i) / (p * r))
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.time_text_input.text = str(t)

    def show_principal(self):
        try:
            i = float(self.root.ids.principal_i.text)
            t = float(self.root.ids.principal_t.text)
            r = float(self.root.ids.principal_r.text)
            p = float((100 * i) / (r * t))
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.principal_text_input.text = str(p)

    def show_compound_interest(self):
        try:
            P = float(self.root.ids.compound_interest_p.text)
            R = float(self.root.ids.compound_interest_r.text)
            n = float(self.root.ids.compound_interest_n.text)
            A = float(P * (1 + R / 100) ** n)
            C = float(A - P)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.compound_interest_text_input.text = str(C)

    def show_sum_of_interior_angles(self):
        try:
            n = int(self.root.ids.sum_of_interior_angles_sides.text)
            sumOfInteriorAngles = int((n - 2) * 180)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.sum_of_interior_angles_text_input.text = str(sumOfInteriorAngles) + '°'

    def show_modular_arithmetic(self):
        try:
            num = float(self.root.ids.modular_arithmetic_number.text)
            mod = float(self.root.ids.modular_arithmetic_mod.text)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            if num.is_integer() is True:
                modResult = int(num % mod)
                self.root.ids.modular_arithmetic_text_input.text = str(modResult) + '(mod' + str(mod) + ')'
            else:
                modResult = fmod(num, mod)
                self.root.ids.modular_arithmetic_text_input.text = str(modResult) + '(mod' + str(mod) + ')'

    def show_pythagoras_theorem_two_side_hypotenuse(self):
        try:
            opp = float(self.root.ids.two_side_hypotenuse_opposite.text)
            adj = float(self.root.ids.two_side_hypotenuse_adjacent.text)
            hyp_fk = (opp ** 2) + (adj ** 2)
            hyp = sqrt(hyp_fk)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            if hyp.is_integer() is True:
                self.root.ids.pythagoras_theorem_two_side_hypotenuse_text_input.text = str(int(hyp))
            elif hyp.is_integer() is False:
                hyp_st = str(float(hyp))
                hyp_new = hyp_st[:hyp_st.index('.') + 3]
                self.root.ids.pythagoras_theorem_two_side_hypotenuse_text_input.text = \
                    '√' + str(hyp_fk) + ' or ' + str(hyp_new)

    def show_pythagoras_theorem_two_side_opposite(self):
        try:
            adj = float(self.root.ids.two_side_opposite_adjacent.text)
            hyp = float(self.root.ids.two_side_opposite_hypotenuse.text)
            oppSq = (hyp ** 2) - (adj ** 2)
            opp = sqrt(oppSq)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            if opp.is_integer() is True:
                self.root.ids.pythagoras_theorem_two_side_opposite_text_input.text = str(int(opp))
            elif opp.is_integer() is False:
                opp_st = str(float(hyp))
                opp_new = opp_st[:opp_st.index('.') + 4]
                self.root.ids.pythagoras_theorem_two_side_opposite_text_input.text = \
                    '√' + str(oppSq) + ' or ' + str(opp_new)

    def show_pythagoras_theorem_two_side_adjacent(self):
        try:
            opp = float(self.root.ids.two_side_adjacent_opposite.text)
            hyp = float(self.root.ids.two_side_adjacent_hypotenuse.text)
            adjSq = (hyp ** 2) - (opp ** 2)
            adj = sqrt(adjSq)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            if adj.is_integer() is True:
                self.root.ids.pythagoras_theorem_two_side_adjacent_text_input.text = str(int(opp))
            elif adj.is_integer() is False:
                adj_st = str(float(adj))
                adj_new = adj_st[:adj_st.index('.') + 4]
                self.root.ids.pythagoras_theorem_two_side_adjacent_text_input.text = \
                    '√' + str(adjSq) + ' or ' + str(adj_new)

    def show_trigonometrical_ratios_opposite_which_hyp(self):
        try:
            hyp = float(self.root.ids.trigonometrical_ratios_opposite_which_hyp_hypotenuse.text)
            angle = float(self.root.ids.trigonometrical_ratios_opposite_which_hyp_angle.text)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            if self.root.ids.trig_opp_hyp_rad_checkbox.active is True:
                opp = math.sin(angle) * hyp
                self.root.ids.trigonometrical_ratios_opposite_which_hyp_text_input.text = str(opp)
            elif self.root.ids.trig_opp_hyp_deg_checkbox.active is True:
                opp = math.sin(rad_to_deg(angle)) * hyp
                self.root.ids.trigonometrical_ratios_opposite_which_hyp_text_input.text = str(opp)
            elif self.root.ids.trig_opp_hyp_rad_checkbox.active and self.root.ids.trig_opp_hyp_deg_checkbox.active \
                    is False:
                toast('pick between RAD or DEG and enter all the values correctly')

    def show_trigonometrical_ratios_opposite_which_adj(self):
        try:
            adj = float(self.root.ids.trigonometrical_ratios_opposite_which_adj_adjacent.text)
            angle = float(self.root.ids.trigonometrical_ratios_opposite_which_adj_angle.text)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            if self.root.ids.trig_opp_adj_rad_checkbox.active is True:
                opp = (math.tan(angle)) * adj
                self.root.ids.trigonometrical_ratios_opposite_which_adj_text_input.text = str(opp)
            elif self.root.ids.trig_opp_adj_deg_checkbox.active is True:
                opp = math.tan(rad_to_deg(angle)) * adj
                self.root.ids.trigonometrical_ratios_opposite_which_adj_text_input.text = str(opp)
            elif self.root.ids.trig_opp_adj_rad_checkbox.active and self.root.ids.trig_opp_adj_deg_checkbox.active \
                    is False:
                toast('pick between RAD or DEG and enter all the values correctly')

    def show_trigonometrical_ratios_hypotenuse_which_opp(self):
        try:
            opp = float(self.root.ids.trigonometrical_ratios_hypotenuse_which_opp_opposite.text)
            angle = float(self.root.ids.trigonometrical_ratios_hypotenuse_which_opp_angle.text)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            if self.root.ids.trig_hyp_opp_rad_checkbox.active is True:
                hyp = opp / (math.sin(angle))
                self.root.ids.trigonometrical_ratios_hypotenuse_which_opp_text_input.text = str(hyp)
            elif self.root.ids.trig_hyp_opp_deg_checkbox.active is True:
                hyp = opp / math.sin(rad_to_deg(angle))
                self.root.ids.trigonometrical_ratios_hypotenuse_which_opp_text_input.text = str(hyp)
            elif self.root.ids.trig_hyp_opp_rad_checkbox.active and self.root.ids.trig_hyp_opp_deg_checkbox.active \
                    is False:
                toast('pick between RAD or DEG and enter all the values correctly')

    def show_trigonometrical_ratios_hypotenuse_which_adj(self):
        try:
            adj = float(self.root.ids.trigonometrical_ratios_hypotenuse_which_adj_adjacent.text)
            angle = float(self.root.ids.trigonometrical_ratios_hypotenuse_which_adj_angle.text)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            if self.root.ids.trig_hyp_adj_rad_checkbox.active is True:
                hyp = adj / (math.cos(angle))
                self.root.ids.trigonometrical_ratios_hypotenuse_which_adj_text_input.text = str(hyp)
            elif self.root.ids.trig_hyp_adj_deg_checkbox.active is True:
                hyp = adj / (math.cos(rad_to_deg(angle)))
                self.root.ids.trigonometrical_ratios_hypotenuse_which_adj_text_input.text = str(hyp)
            elif self.root.ids.trig_hyp_adj_rad_checkbox.active and self.root.ids.trig_hyp_adj_deg_checkbox.active \
                    is False:
                toast('pick between RAD or DEG and enter all the values correctly')

    def show_trigonometrical_ratios_adjacent_which_hyp(self):
        try:
            hyp = float(self.root.ids.trigonometrical_ratios_adjacent_which_hyp_hypotenuse.text)
            angle = float(self.root.ids.trigonometrical_ratios_adjacent_which_hyp_angle.text)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            if self.root.ids.trig_adj_hyp_rad_checkbox.active is True:
                adj = math.cos(angle) * hyp
                self.root.ids.trigonometrical_ratios_adjacent_which_hyp_text_input.text = str(adj)
            elif self.root.ids.trig_adj_hyp_deg_checkbox.active is True:
                adj = math.cos(rad_to_deg(angle)) * hyp
                self.root.ids.trigonometrical_ratios_adjacent_which_hyp_text_input.text = str(adj)
            elif self.root.ids.trig_adj_hyp_rad_checkbox.active and self.root.ids.trig_adj_hyp_deg_checkbox.active \
                    is False:
                toast('pick between RAD or DEG and enter all the values correctly')

    def show_trigonometrical_ratios_adjacent_which_opp(self):
        try:
            opp = float(self.root.ids.trigonometrical_ratios_adjacent_which_opp_opposite.text)
            angle = float(self.root.ids.trigonometrical_ratios_adjacent_which_opp_angle.text)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            if self.root.ids.trig_adj_opp_rad_checkbox.active is True:
                adj = opp / (math.tan(angle))
                self.root.ids.trigonometrical_ratios_adjacent_which_opp_text_input.text = str(adj)
            elif self.root.ids.trig_adj_opp_deg_checkbox.active is True:
                adj = opp / (math.tan(rad_to_deg(angle)))
                self.root.ids.trigonometrical_ratios_adjacent_which_opp_text_input.text = str(adj)
            elif self.root.ids.trig_adj_opp_rad_checkbox.active and self.root.ids.trig_adj_opp_deg_checkbox.active \
                    is False:
                toast('pick between RAD or DEG and enter all the values correctly')

    def show_linear_equation(self):
        try:
            equ = self.root.ids.linear_equation.text
            equ = equ.split(maxsplit=1)
            equ_one = eval(equ[1])
            equ_two = equ[0]
            equ_two = equ_two[0:equ_two.index('x')]
            sol = float(equ_one) / float(equ_two)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        except IndexError:
            toast('give a space after the variable,e.g 2x -1 +2')
        except SyntaxError:
            toast('all inputs are assumed to equal to zero, so write your equations like this, 2x -1+2-4')
        else:
            self.root.ids.linear_equation_text_input.text = str(sol)

    def show_quadratic_equation(self):
        try:
            equ = self.root.ids.quadratic_equation.text
            equ = equ.split(maxsplit=2)
            x = equ[0]
            a = int(x[0:x.index('x^2')])
            x_two_in_equ = equ[1]
            b = int(x_two_in_equ[0:x_two_in_equ.index('x')])
            c = int(eval(equ[2]))
            d = (b ** 2) - (4 * a * c)
            sol1 = (-b - math.sqrt(d) / (2 * a))
            sol2 = (-b + math.sqrt(d) / (2 * a))
            sol = 'x1=' + str(sol1) + ' x2=' + str(sol2)
        except ValueError:
            toast('correct values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        except IndexError:
            toast('give a space after the variable,e.g 2x^2 -1x +2')
        except SyntaxError:
            toast('all inputs are assumed to equal to zero, so write your equations like this, 2x^2 -1x +2-4')
        except Exception as q:
            toast('error message:' + str(q))
        else:
            self.root.ids.quadratic_equation_text_input.text = str(sol)

    def show_simultaneous_equation(self):
        try:
            equ = self.root.ids.simultaneous_equation_first.text
            equ1 = self.root.ids.simultaneous_equation_second.text
            equ = equ.split(maxsplit=3)
            equ1 = equ1.split(maxsplit=3)
            x = equ[0]
            x_dig = x[0:x.index('x')]
            y = equ[1]
            y_dig = y[0:y.index('y')]
            x_two = equ1[0]
            x_dig_two = x_two[0:x_two.index('x')]
            y_two = equ1[1]
            y_dig_two = y_two[0:y_two.index('y')]
            x_dig_three = eval(equ[3])
            y_dig_three = eval(equ1[3])
            a = np.array([[int(x_dig), int(y_dig)], [int(x_dig_two), int(y_dig_two)]])
            b = np.array([int(x_dig_three), int(y_dig_three)])
            z = np.linalg.solve(a, b)
            sol = z
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        except IndexError:
            toast('give a space after the variable,e.g 2x -1y = +2, give appropriate spacing')
        except SyntaxError:
            toast('write your equations like this, 2x -1y = -4')
        except Exception as q:
            toast('error message:' + str(q))
        else:
            self.root.ids.simultaneous_equation_text_input.text = str(sol)

    def show_quadratic_equations_from_roots(self):
        try:
            firstRoot = float(self.root.ids.quadratic_equations_first.text)
            secondRoot = float(self.root.ids.quadratic_equations_second.text)
            sumOfRoots = int(-1 * (firstRoot + secondRoot))
            productOfRoots = int(firstRoot * secondRoot)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            if sumOfRoots < 0 and productOfRoots < 0:
                self.root.ids.quadratic_equations_from_roots_text_input.text = \
                    'x^2' + str(sumOfRoots) + 'x ' + str(productOfRoots)
            elif sumOfRoots > 0 and productOfRoots > 0:
                self.root.ids.quadratic_equations_from_roots_text_input.text = \
                    ('x^2+' + str(sumOfRoots) + 'x +' + str(productOfRoots))
            elif sumOfRoots < 0 and productOfRoots > 0:
                self.root.ids.quadratic_equations_from_roots_text_input.text = \
                    ('x^2' + str(sumOfRoots) + 'x +' + str(productOfRoots))
            elif sumOfRoots > 0 and productOfRoots < 0:
                self.root.ids.quadratic_equations_from_roots_text_input.text = \
                    ('x^2+' + str(sumOfRoots) + 'x ' + str(productOfRoots))

    def show_distance(self):
        try:
            time = float(self.root.ids.distance_time.text)
            speed = float(self.root.ids.distance_speed.text)
            distance = float(speed * time)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.distance_text_input.text = str(distance)

    def show_time_in_distance(self):
        try:
            speed = float(self.root.ids.time_speed.text)
            distance = float(self.root.ids.time_distance.text)
            time = float(distance / speed)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.time_in_distance_text_input.text = str(time)

    def show_speed(self):
        try:
            distance = float(self.root.ids.speed_distance.text)
            time = float(self.root.ids.speed_time.text)
            speed = float(distance / time)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.speed_text_input.text = str(speed)

    def show_percentage_profit(self):
        try:
            profit = float(self.root.ids.percentage_profit_profit.text)
            cost_price = float(self.root.ids.percentage_profit_cost_price.text)
            percentageProfit = float((profit * 100) / cost_price)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.percentage_profit_text_input.text = str(percentageProfit) + '%'

    def show_percentage_loss(self):
        try:
            loss = float(self.root.ids.percentage_loss_loss.text)
            cost_price = float(self.root.ids.percentage_loss_cost_price.text)
            percentage_loss = float((loss * 100) / cost_price)
        except ValueError:
            toast('values are required')
        except ZeroDivisionError:
            toast('Zero can’t be a denominator.')
        else:
            self.root.ids.percentage_loss_text_input.text = str(percentage_loss) + '%'

    def show_mean(self):
        try:
            numbers = self.root.ids.mean.text
            numbers = numbers.split(',')
            while numbers.count(',') != 0:
                del numbers[numbers.index(',')]
            for n in numbers:
                numbers[numbers.index(n)] = int(n)
            result = mean(numbers)
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.mean_text_input.text = str(result)

    def show_median(self):
        try:
            numbers = self.root.ids.median.text
            numbers = numbers.split(',')
            while numbers.count(',') != 0:
                del numbers[numbers.index(',')]
            for n in numbers:
                numbers[numbers.index(n)] = int(n)
            result = median(numbers)
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.median_text_input.text = str(result)

    def show_mode(self):
        try:
            numbers = self.root.ids.mode.text
            numbers = numbers.split(',')
            while numbers.count(',') != 0:
                del numbers[numbers.index(',')]
            for n in numbers:
                numbers[numbers.index(n)] = int(n)
            result = mode(numbers)
        except ValueError:
            toast('values are required')
        else:
            self.root.ids.mode_text_input.text = str(result)


if __name__ == '__main__':
    app = CalculateAllApp()
    app.run()
