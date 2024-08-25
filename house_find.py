import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QDialog, QFormLayout, QTextBrowser, QComboBox

# Mock user data
user_credentials = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

# Mock state data with district-wise house prices
state_data = {
    "Andhra Pradesh": {
        "Amaravati": "₹90,00,000",
        "Visakhapatnam": "₹85,00,000",
        "Vijayawada": "₹82,00,000",
        "Guntur": "₹78,00,000",
        "Nellore": "₹72,00,000",
    },
    "Arunachal Pradesh": {
        "Itanagar": "₹68,00,000",
        "Tawang": "₹75,00,000",
        "Naharlagun": "₹70,00,000",
        "Pasighat": "₹72,00,000",
        "Bomdila": "₹65,00,000",
    },
    "Assam": {
        "Guwahati": "₹78,00,000",
        "Dibrugarh": "₹72,00,000",
        "Silchar": "₹68,00,000",
        "Jorhat": "₹75,00,000",
        "Nagaon": "₹70,00,000",
    },
    "Bihar": {
        "Patna": "₹78,00,000",
        "Gaya": "₹72,00,000",
        "Bhagalpur": "₹68,00,000",
        "Muzaffarpur": "₹75,00,000",
        "Darbhanga": "₹70,00,000",
    },
    "Chhattisgarh": {
        "Raipur": "₹70,00,000",
        "Bhilai": "₹75,00,000",
        "Bilaspur": "₹68,00,000",
        "Korba": "₹72,00,000",
        "Raigarh": "₹65,00,000",
    },
    "Goa": {
        "Panaji": "₹85,00,000",
        "Vasco da Gama": "₹82,00,000",
        "Margoa": "₹78,00,000",
        "Mapusa": "₹80,00,000",
        "Ponda": "₹75,00,000",
    },
    "Gujarat": {
        "Ahmedabad": "₹90,00,000",
        "Surat": "₹88,00,000",
        "Vadodara": "₹80,00,000",
        "Rajkot": "₹75,00,000",
        "Gandhinagar": "₹92,00,000",
    },
    "Haryana": {
        "Chandigarh": "₹85,00,000",
        "Faridabad": "₹82,00,000",
        "Gurgaon": "₹78,00,000",
        "Panipat": "₹80,00,000",
        "Ambala": "₹75,00,000",
    },
    "Himachal Pradesh": {
        "Shimla": "₹70,00,000",
        "Dharamshala": "₹72,00,000",
        "Mandi": "₹68,00,000",
        "Solan": "₹75,00,000",
        "Kullu": "₹70,00,000",
    },
    "Jharkhand": {
        "Ranchi": "₹70,00,000",
        "Jamshedpur": "₹75,00,000",
        "Dhanbad": "₹68,00,000",
        "Bokaro": "₹72,00,000",
        "Hazaribagh": "₹65,00,000",
    },
    "Karnataka": {
        "Bangalore": "₹85,00,000",
        "Mysore": "₹70,00,000",
        "Hubli": "₹65,00,000",
        "Mangalore": "₹90,00,000",
        "Belgaum": "₹60,00,000",
    },
    "Kerala": {
        "Thiruvananthapuram": "₹85,00,000",
        "Kochi": "₹88,00,000",
        "Kozhikode": "₹82,00,000",
        "Thrissur": "₹78,00,000",
        "Kollam": "₹72,00,000",
    },
    "Madhya Pradesh": {
        "Bhopal": "₹70,00,000",
        "Indore": "₹75,00,000",
        "Gwalior": "₹68,00,000",
        "Jabalpur": "₹72,00,000",
        "Ujjain": "₹65,00,000",
    },
    "Maharashtra": {
        "Mumbai": "₹1,00,00,000",
        "Pune": "₹90,00,000",
        "Nagpur": "₹85,00,000",
        "Aurangabad": "₹75,00,000",
        "Thane": "₹95,00,000",
    },
    "Manipur": {
        "Imphal": "₹75,00,000",
        "Bishnupur": "₹70,00,000",
        "Thoubal": "₹68,00,000",
        "Churachandpur": "₹72,00,000",
        "Senapati": "₹65,00,000",
    },
    "Meghalaya": {
        "Shillong": "₹78,00,000",
        "Tura": "₹72,00,000",
        "Jowai": "₹68,00,000",
        "Nongstoin": "₹75,00,000",
        "Williamnagar": "₹70,00,000",
    },
    "Mizoram": {
        "Aizawl": "₹75,00,000",
        "Lunglei": "₹70,00,000",
        "Saiha": "₹68,00,000",
        "Champhai": "₹72,00,000",
        "Serchhip": "₹65,00,000",
    },
    "Nagaland": {
        "Kohima": "₹78,00,000",
        "Dimapur": "₹72,00,000",
        "Mokokchung": "₹68,00,000",
        "Tuensang": "₹75,00,000",
        "Zunheboto": "₹70,00,000",
    },
    "Odisha": {
        "Bhubaneswar": "₹85,00,000",
        "Cuttack": "₹82,00,000",
        "Rourkela": "₹78,00,000",
        "Berhampur": "₹80,00,000",
        "Sambalpur": "₹75,00,000",
    },
    "Punjab": {
        "Amritsar": "₹70,00,000",
        "Ludhiana": "₹75,00,000",
        "Jalandhar": "₹68,00,000",
        "Patiala": "₹72,00,000",
        "Bathinda": "₹65,00,000",
    },
    "Rajasthan": {
        "Jaipur": "₹80,00,000",
        "Jodhpur": "₹75,00,000",
        "Udaipur": "₹72,00,000",
        "Kota": "₹70,00,000",
        "Ajmer": "₹68,00,000",
    },
    "Sikkim": {
        "Gangtok": "₹80,00,000",
        "Namchi": "₹75,00,000",
        "Mangan": "₹72,00,000",
        "Gyalshing": "₹70,00,000",
        "Singtam": "₹68,00,000",
    },
    "Tamil Nadu": {
        "Chennai": "₹80,00,000",
        "Coimbatore": "₹75,00,000",
        "Madurai": "₹65,00,000",
        "Trichy": "₹70,00,000",
        "Salem": "₹55,00,000",
    },
    "Telangana": {
        "Hyderabad": "₹95,00,000",
        "Warangal": "₹88,00,000",
        "Nizamabad": "₹82,00,000",
        "Khammam": "₹78,00,000",
        "Karimnagar": "₹72,00,000",
    },
    "Tripura": {
        "Agartala": "₹70,00,000",
        "Udaipur": "₹75,00,000",
        "Dharmanagar": "₹68,00,000",
        "Ambassa": "₹72,00,000",
        "Kailasahar": "₹65,00,000",
    },
    "Uttar Pradesh": {
        "Lucknow": "₹75,00,000",
        "Kanpur": "₹70,00,000",
        "Varanasi": "₹68,00,000",
        "Agra": "₹72,00,000",
        "Allahabad": "₹65,00,000",
    },
    "Uttarakhand": {
        "Dehradun": "₹80,00,000",
        "Haridwar": "₹75,00,000",
        "Rishikesh": "₹72,00,000",
        "Nainital": "₹70,00,000",
        "Almora": "₹68,00,000",
    },
    "West Bengal": {
        "Kolkata": "₹75,00,000",
        "Durgapur": "₹60,00,000",
        "Asansol": "₹58,00,000",
        "Siliguri": "₹62,00,000",
        "Howrah": "₹70,00,000",
    },
}

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("House Price Checker")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.signup_button = QPushButton("Sign Up", self)
        self.signup_button.clicked.connect(self.show_signup_dialog)
        self.layout.addWidget(self.signup_button)

        self.signin_button = QPushButton("Sign In", self)
        self.signin_button.clicked.connect(self.show_signin_dialog)
        self.layout.addWidget(self.signin_button)

        self.central_widget.setLayout(self.layout)

    def show_signup_dialog(self):
        signup_dialog = SignupDialog(self)
        result = signup_dialog.exec_()

        if result == QDialog.Accepted:
            username = signup_dialog.username_input.text()
            state_prices_window = StatePricesWindow(username)
            state_prices_window.exec_()

    def show_signin_dialog(self):
        signin_dialog = SigninDialog(self)
        signin_dialog.exec_()

class SignupDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Sign Up")

        layout = QFormLayout()

        self.username_input = QLineEdit(self)
        layout.addRow("Username:", self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addRow("Password:", self.password_input)

        self.signup_button = QPushButton("Sign Up", self)
        self.signup_button.clicked.connect(self.signup)
        layout.addWidget(self.signup_button)

        self.setLayout(layout)

    def signup(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username in user_credentials:
            QMessageBox.warning(self, "Sign Up Error", "Username already exists. Please choose a different one.")
        else:
            user_credentials[username] = password
            QMessageBox.information(self, "Sign Up Successful", "Account created successfully. You can now sign in.")
            self.accept()

class SigninDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Sign In")

        layout = QFormLayout()

        self.username_input = QLineEdit(self)
        layout.addRow("Username:", self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addRow("Password:", self.password_input)

        self.signin_button = QPushButton("Sign In", self)
        self.signin_button.clicked.connect(self.signin)
        layout.addWidget(self.signin_button)

        self.forgot_password_button = QPushButton("Forgot Password", self)
        self.forgot_password_button.clicked.connect(self.show_forgot_password_dialog)
        layout.addWidget(self.forgot_password_button)

        self.setLayout(layout)

    def signin(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username in user_credentials and user_credentials[username] == password:
            QMessageBox.information(self, "Sign In Successful", f"Welcome, {username}!")
            self.accept()
            self.show_state_prices(username)
        else:
            QMessageBox.warning(self, "Sign In Error", "Invalid username or password.")

    def show_forgot_password_dialog(self):
        forgot_password_dialog = ForgotPasswordDialog(self)
        forgot_password_dialog.exec_()

    def show_state_prices(self, username):
        state_prices_window = StatePricesWindow(username)
        state_prices_window.exec_()

class ForgotPasswordDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Forgot Password")

        layout = QFormLayout()

        self.username_input = QLineEdit(self)
        layout.addRow("Username:", self.username_input)

        self.new_password_input = QLineEdit(self)
        self.new_password_input.setEchoMode(QLineEdit.Password)
        layout.addRow("New Password:", self.new_password_input)

        self.reset_password_button = QPushButton("Reset Password", self)
        self.reset_password_button.clicked.connect(self.reset_password)
        layout.addWidget(self.reset_password_button)

        self.setLayout(layout)

    def reset_password(self):
        username = self.username_input.text()
        new_password = self.new_password_input.text()

        if username in user_credentials:
            user_credentials[username] = new_password
            QMessageBox.information(self, "Password Reset", "Password reset successfully.")
            self.accept()
        else:
            QMessageBox.warning(self, "Reset Password Error", "Username not found.")

class StatePricesWindow(QDialog):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("Indian States and District-wise House Prices")

        layout = QVBoxLayout()

        state_prices_label = QLabel("State-wise House Prices in India")
        layout.addWidget(state_prices_label)

        self.city_combobox = QComboBox(self)
        self.city_combobox.addItem("Select City")
        self.city_combobox.addItems(state_data.keys())
        layout.addWidget(self.city_combobox)

        self.district_combobox = QComboBox(self)
        self.district_combobox.addItem("Select District")
        layout.addWidget(self.district_combobox)

        self.state_prices_text = QTextBrowser(self)
        layout.addWidget(self.state_prices_text)

        self.show_prices_button = QPushButton("Show Prices", self)
        self.show_prices_button.clicked.connect(self.show_prices)
        layout.addWidget(self.show_prices_button)

        self.setLayout(layout)

        # Connect the city_combobox to update district_combobox
        self.city_combobox.currentIndexChanged.connect(self.update_district_combobox)

    def update_district_combobox(self):
        selected_city = self.city_combobox.currentText()
        self.district_combobox.clear()
        self.district_combobox.addItem("Select District")
        self.district_combobox.addItems(state_data.get(selected_city, {}).keys())

    def show_prices(self):
        selected_city = self.city_combobox.currentText()
        selected_district = self.district_combobox.currentText()

        if selected_city == "Select City" or selected_district == "Select District":
            QMessageBox.warning(self, "Price Lookup Error", "Please select a city and district to view house prices.")
        else:
            district_prices = state_data.get(selected_city, {}).get(selected_district, "Not Available")
            self.state_prices_text.setPlainText(f"House Price in {selected_district}, {selected_city}: {district_prices}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
