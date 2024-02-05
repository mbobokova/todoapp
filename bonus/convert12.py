import PySimpleGUI as sg

# First line
feet_label = sg.Text('Enter feet: ')
feet_input = sg.Input()


# Second line
inches_label = sg.Text('Enter inches: ')
inches_input = sg.Input()


convert_button = sg.Button("convert")


window = sg.Window('Convertor',
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [convert_button]]
                   )

window.read()
window.close()


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters
