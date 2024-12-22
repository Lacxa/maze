import os
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy import platform

if platform == "android":
    from jnius import autoclass
    from android.permissions import request_permissions, Permission



class GhApp(MDApp):
    def build(self):
        if platform == "android":
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])


    def generate_pdf(self):
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        filename = f"report_{timestamp}.pdf"
        filepath = os.path.join(self.user_data_dir, filename)  # saves file in app data directory
        try:
            c = canvas.Canvas(filepath, pagesize=letter)
            # Add content to the PDF (replace with your actual data)
            c.drawString(72, 750, "This is a simple report.")  # Example content
            c.save()
            self.root.ids.filename_label.text = filename
            print(f"Report saved to: {filepath}")
            return filepath
        except Exception as e:
            print(f"Error generating report: {e}")
            return None

    def share_whatsapp(self):
        filepath = self.generate_pdf()
        if filepath and platform == "android":
            try:
                PythonActivity = autoclass("org.kivy.android.PythonActivity")
                Intent = autoclass("android.content.Intent")
                Uri = autoclass("android.net.Uri")
                File = autoclass("java.io.File")

                intent = Intent(Intent.ACTION_SEND)
                intent.setType("application/pdf")

                file = File(filepath)
                uri = Uri.fromFile(file)
                intent.putExtra(Intent.EXTRA_STREAM, uri)
                intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)

                chooser = Intent.createChooser(intent, "Share PDF")
                PythonActivity.mActivity.startActivity(chooser)
            except Exception as e:
                print(f"Error sharing: {e}")
        elif filepath:
            print("Sharing is only available on Android devices")
        else:
            print("No file was created")


GhApp().run()