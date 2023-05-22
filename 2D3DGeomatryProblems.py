import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap

class GeometrySimulator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Geometry Simulator')
        self.setGeometry(100, 100, 700, 500)

        # Create a label for the shape selector
        self.shape_label = QLabel('Select a shape:', self)
        self.shape_label.move(20, 20)

        # Create a combo box for shape selection
        self.shape_combo = QComboBox(self)
        self.shape_combo.addItem('Triangle')
        self.shape_combo.addItem('Rectangle')
        self.shape_combo.addItem('Square')
        self.shape_combo.addItem('Circle')
        self.shape_combo.addItem('Trapezoid')
        self.shape_combo.addItem('Cube')
        self.shape_combo.addItem('Sphere')
        self.shape_combo.addItem('Cylinder')
        self.shape_combo.addItem('Cone')
        self.shape_combo.addItem('Pyramid')
        self.shape_combo.move(20, 50)
        self.shape_combo.currentIndexChanged.connect(self.shape_changed)

        # Create a label for the image of the shape
        self.shape_image_label = QLabel(self)
        self.shape_image_label.move(200, 400)

        # Create a label for the rules and formulas
        self.rules_label = QLabel('Rules and Formulas:', self)
        self.rules_label.move(20, 150)

        # Create a text box for the rules and formulas
        self.rules_textbox = QLineEdit(self)
        self.rules_textbox.setReadOnly(True)
        self.rules_textbox.move(20, 180)
        self.rules_textbox.resize(300, 200)

        # Create a label for the problem-solving section
        self.problem_label = QLabel('Problem-Solving:', self)
        self.problem_label.move(350, 20)

        # Create input fields for the necessary parameters
        self.param1_label = QLabel('Parameter 1:', self)
        self.param1_label.move(350, 50)
        self.param1_textbox = QLineEdit(self)
        self.param1_textbox.move(450, 50)
        self.param1_textbox.resize(100, 30)

        self.param2_label = QLabel('Parameter 2:', self)
        self.param2_label.move(350, 90)
        self.param2_textbox = QLineEdit(self)
        self.param2_textbox.move(450, 90)
        self.param2_textbox.resize(100, 30)

        self.param3_label = QLabel('Parameter 3:', self)
        self.param3_label.move(350, 130)
        self.param3_textbox = QLineEdit(self)
        self.param3_textbox.move(450, 130)
        self.param3_textbox.resize(100, 30)

        # Create a button to solve the problem
        self.solve_button = QPushButton('Solve', self)
        self.solve_button.move(350, 180)
        self.solve_button.clicked.connect(self.solve_problem)

        # Create a label for the solution
        self.solution_label = QLabel('Solution:', self)
        self.solution_label.move(350, 220)

        # Create a text box for the solution
        self.solution_textbox = QLineEdit(self)
        self.solution_textbox.setReadOnly(True)
        self.solution_textbox.move(350, 250)
        self.solution_textbox.resize(300, 130)

        # Show the GUI
        self.show()

    def shape_changed(self):
        # Get the selected shape
        shape = self.shape_combo.currentText()

        # Update the image of the shape
        pixmap = QPixmap('images/' + shape.lower() + '.png')
        self.shape_image_label.setPixmap(pixmap)
        self.shape_image_label.resize(pixmap.width(), pixmap.height())

        # Update the rules and formulas
        if shape.lower() not in ['triangle', 'rectangle', 'square', 'circle', 'trapezoid', 'cube', 'sphere', 'cylinder', 'cone', 'pyramid']:
            print("sorry this shape is not here, search about it!!")        
        elif shape == 'Triangle':
            self.rules_textbox.setText('- Area= 1/2 * base * height\nArea: 1/2 * base * height\n ')
        elif shape == 'Rectangle':
            self.rules_textbox.setText('Area= length * width \n Perimeter= 2 * (length + width)')
        elif shape == 'Square':
            self.rules_textbox.setText('Area= side^2 \n Perimeter= 4 * side')
        elif shape == 'Circle':
            self.rules_textbox.setText('Area= pi * radius^2 \n Circumference= 2 * pi * radius')
        elif shape == 'Trapezoid':
            self.rules_textbox.setText('Area= 1/2 * (b1 + b2) * h \nPerimeter= a + b1 + b2 + c')
        elif shape == 'Cube':
            self.rules_textbox.setText('- Surface Area=6* area of the base^2\n- (area of the base)^3 ')
        elif shape == 'Sphere':
            self.rules_textbox.setText('- Surface area=side^2\n- Volume= 4 * side')
        elif shape == 'Cylinder':
            self.rules_textbox.setText('- Surface area=2 * pi * radius^2 + 2 * pi * radius * height\n- Volume=pi * radius^2 * height')
        elif shape == 'Cone':
            self.rules_textbox.setText('- Surface area=pi * radius^2 + pi * radius *slant height \n- Volume=\n- (1/3) * pi * radius^2 * Slant height')
        elif shape == 'Pyramid':
            self.rules_textbox.setText('- Surface area=1/2 * length of one of the sides*height + area of the base *  slant height\n- Volume\n-  (1/3) * length of one of the sides*height* slant height')

    def solve_problem(self):
        try:
            # Get the selected shape and parameters
            shape = self.shape_combo.currentText()
            param1 = float(self.param1_textbox.text())
            param2 = float(self.param2_textbox.text())
            param3 = float(self.param3_textbox.text())

            # Solve the problem and update the solution textbox
            if shape == 'Triangle':
                area = 0.5 * param1 * param2
                perimeter = param1 + param2 + param3
                solution = 'Area: {:.2f}\nPerimeter: {:.2f}'.format(area, perimeter)
            elif shape == 'Rectangle':
                area = param1 * param2
                perimeter = 2 * (param1 + param2)
                solution = 'Area: {:.2f}\nPerimeter: {:.2f}'.format(area, perimeter)
            elif shape == 'Square':
                area = param1 ** 2
                perimeter = 4 * param1
                solution = 'Area: {:.2f}\nPerimeter: {:.2f}'.format(area, perimeter)
            elif shape == 'Circle':
                area = 3.14 * param1 ** 2
                circumference = 2 * 3.14 * param1
                solution = 'Area: {:.2f}\nCircumference: {:.2f}'.format(area, circumference)
            elif shape == 'Trapezoid':
                area = 0.5 * (param1 + param2) * param3
                solution = 'Area: {:.2f}'.format(area)
            elif shape == 'Cube':
                surface_area = 6 * param1 ** 2
                volume = param1 ** 3
                solution = 'Surface Area: {:.2f}\nVolume: {:.2f}'.format(surface_area, volume)
            elif shape == 'Sphere':
                surface_area = 4 * 3.14 * param1 ** 2
                volume = (4 / 3) * 3.14 * param1 ** 3
                solution = 'Surface Area: {:.2f}\nVolume: {:.2f}'.format(surface_area, volume)
            elif shape == 'Cylinder':
                surface_area = (2 * 3.14 * param1 * param2) + (2 * 3.14 * param1 ** 2)
                volume = 3.14 * param1 ** 2 * param2
                solution = 'Surface Area: {:.2f}\nVolume: {:.2f}'.format(surface_area, volume)
            elif shape == 'Cone':
                surface_area = 3.14 * param1 * (param1 + param2)
                volume = (1 / 3) * 3.14 * param1 ** 2 * param3
                solution = 'Surface Area: {:.2f}\nVolume: {:.2f}'.format(surface_area, volume)
            elif shape == 'Pyramid':
                surface_area = (param1 * param2) + param1 * ((param3 ** 2) + (param2 ** 2)) ** 0.5
                volume = (1 / 3) * param1 * param2 * param3
                solution = 'Surface Area: {:.2f}\nVolume: {:.2f}'.format(surface_area, volume)

            self.solution_textbox.setText(solution)

        except ValueError:
            self.solution_textbox.setText('Invalid input. Please enter valid numbers for the parameters.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GeometrySimulator()
    sys.exit(app.exec_())