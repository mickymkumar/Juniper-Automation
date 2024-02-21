import backend.configs.package as module


class MyApplication(module.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Testing Application")
        self.resize(800, 600)

        self.create_menubar()
        self.create_toolbar()
        self.html_output()

    def create_menubar(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        file_menu.addAction("Exit")

        #run_menu = menubar.addMenu("Run")
        #run_menu.addAction("All Test cases")
        #run_menu.addAction("API Test Cases")
        #run_menu.addAction("5G")

    def create_toolbar(self):
        toolbar = self.addToolBar("Toolbar")

        alltcbutton = module.QPushButton("Run All Testcase")
        APITCbutton = module.QPushButton("Run API Test Cases")

        toolbar.addWidget(alltcbutton)
        toolbar.addWidget(APITCbutton)

        def run_tests(self):
            suite = module.unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
            result = module.unittest.TextTestRunner().run(suite)

            with open("result.html", "w") as file:
                file.write(self.html_output(result))

    def html_output(self):
        layout = module.QVBoxLayout()

        text_edit = module.QTextEdit()
        text_edit.setReadOnly(True)
        layout.addWidget(text_edit)

        html_report = "<div style='text-align:center;color:gray;font-size:12px;'>" \
                        "<h1>Dashboard</h1>" \
                        "<table>"\
                          "<tr>" \
                            "<th>Date</th>"\
                            "<th>Status</th>"\
                          "</tr>"\
                          "<tr>"\
                            "<td><script>" \
                            "module.datetime.today()"\
                            "</script></td>"\
                            "<td> </td>"\
                          "</tr>"\
                        "</table>" \
                        "<html><body>" \
                        "<h1>Test Results</h1>" \
                        "<ul>" \
                      "<script> for test_case in result.failures + result.errors:" \
                      "<li>{} - {}</li>.format(test_case[0], test_case[1]) </script>" \
                    "</ul>" \
                "</body></html>" \
            "</div>"


        text_edit.setHtml(html_report)

        central_widget = module.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Create footer label
        footer_label = module.QLabel("Tester Application")
        footer_label.setAlignment(module.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(footer_label)

class MyTestCase(module.unittest.TestCase):
    #In discussion...
    pass


if __name__ == "__main__":
    app = module.QApplication(module.sys.argv)
    window = MyApplication()
    window.show()
    module.sys.exit(app.exec())
