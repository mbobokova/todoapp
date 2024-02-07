import PySimpleGUI as sg

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


# First line
feet_label = sg.Text('Enter feet: ')
feet_input = sg.Input(key="feet")


# Second line
inches_label = sg.Text('Enter inches: ')
inches_input = sg.Input(key="inches")


convert_button = sg.Button("convert")
convert_result = sg.Text(key='result', text_color='green')


window = sg.Window('Convertor',
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [convert_button, convert_result]]
                   )

while True:
    x, to_convert = window.read()
    print(to_convert)
    feet = int(to_convert["feet"])
    inches = int(to_convert["inches"])
    convert_result = convert(feet, inches)
    convert_result = f"{convert_result} meters"
    window["result"].update(value=convert_result)


window.read()
window.close()


