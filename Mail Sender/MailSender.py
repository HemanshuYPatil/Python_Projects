from cgitb import grey
import tkinter as tk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter.messagebox

def send_mail():
    name = sender_entry.get()
    sub = subject_entry.get()
    message = message_entry.get("1.0",'end-1c')

    list_of_emails = ['hemanshuypatil@gmail.com',
                      'jayashriypatil@gmail.com']
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("hemanshuypatil@gmail.com", "wrczzavnxjojffoe")

    from_ = "hemanshuypatil@gmail.com"
    subject = sub
    html = """
    <html>
    <head>
    </head>
    <body>
    <h3>From """ + name + """ </h3>
    <h4>""" + message + """</h4>
    </body>
    </html>
    """

    for email in list_of_emails:
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = from_
        message["To"] = email

        text = MIMEText(html, "html")
        message.attach(text)

        try:
            server.sendmail(from_, email, message.as_string())
            tkinter.messagebox.showinfo("Success","Mail has sent to all Email Id")
        except Exception as e:
            tkinter.messagebox.showerror("Error","Mail has not sent")

    server.quit()


root = tk.Tk()
root.withdraw()
screen_width = root.winfo_screenwidth()
root.resizable(width=False, height=False)
screen_height = root.winfo_screenheight()
frame_width = 500
frame_height = 500
x_coordinate = (screen_width/2) - (frame_width/2)
y_coordinate = (screen_height/2) - (frame_height/2) 
root.geometry("%dx%d+%d+%d" % (frame_width, frame_height, x_coordinate, y_coordinate))
root.deiconify()
root.title("Email Sender")
root.geometry("600x500")
frame = tk.Frame(root, bg="#000000")

sender_label = tk.Label(root, text="Email Sender", font=("Times New Roman", 20, "italic"))
sender_label.place(x=230, y=21)

sender_label = tk.Label(root, text="Sender name:",font=12)
sender_label.place(x=120,y=100)

sender_entry = tk.Entry(root, font=("Helvetica", 12))
sender_entry.place(x=240,y=97,height=32,width=250)

subject_label = tk.Label(root, text="Subject:",font=12)
subject_label.place(x=120,y=170)

subject_entry = tk.Entry(root, font=("Helvetica", 12))
subject_entry.place(x=240,y=167,height=32,width=250)


message_label = tk.Label(root, text="Message:",font=12)
message_label.place(x=120,y=240)

text_area = tk.Text(root, height=10, width=50 ,font=(12))
text_area.pack(pady=100)
message_entry = tk.Entry(root, font=("Helvetica", 14))
text_area.place(x=240, y=237, height=130, width=250)

message_entry =text_area

send_button = tk.Button(root, text="Send", command=send_mail, bg="black", fg="white",width=12,height=1,font=10)
send_button.place(x=170,y=420)

exit_button = tk.Button(root, text="Exit", command=root.quit, bg="black", fg="white", width=12, height=1, font=10)
exit_button.place(x=350,y=420)


root.mainloop()




 