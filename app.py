import tkinter as tk
from tkinter import ttk, messagebox
import cv2
import numpy as np
from PIL import Image, ImageTk
from datetime import datetime
from database import Database
import os


class AttendanceSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Smart Attendance System")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f0f0f0")

        # Center the window
        self.center_window()

        # Initialize database
        self.db = Database()

        # Initialize face detector
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


        # Configure styles
        self.configure_styles()

        # Create main container
        self.create_main_page()

    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'+{x}+{y}')

    def configure_styles(self):
        """Configure custom styles for the application"""
        style = ttk.Style()

        # Main frame style
        style.configure("Main.TFrame", background="#f0f0f0")

        # Title style
        style.configure("Title.TLabel",
                        font=("Segoe UI", 32, "bold"),
                        background="#f0f50f0",
                        foreground="#2c3e50")

        # Button styles - Improved visibility
        style.configure("Primary.TButton",
                        font=("Segoe UI", 12, "bold"),
                        padding=12,
                        foreground="white",
                        background="#3498db",
                        bordercolor="#3498db",
                        relief="raised",
                        borderwidth=3)

        style.map("Primary.TButton",
                  background=[('active', '#2980b9'), ('pressed', '#1a5276')],
                  foreground=[('active', 'white')],
                  relief=[('active', 'sunken'), ('pressed', 'sunken')])

        style.configure("Secondary.TButton",
                        font=("Segoe UI", 12,"bold"),
                        padding=10,
                        foreground="#2c3e50",
                        background="#ecf0f1",
                        bordercolor="#bdc3c7",
                        relief="raised",
                        borderwidth=2)

        style.map("Secondary.TButton",
                  background=[('active', '#d5dbdb'), ('pressed', '#bdc3c7')],
                  foreground=[('active', '#2c3e50')],
                  relief=[('active', 'sunken'), ('pressed', 'sunken')])

        style.configure("Danger.TButton",
                        font=("Segoe UI", 14, "bold"),
                        padding=10,
                        foreground="white",
                        background="#e74c3c",
                        bordercolor="#e74c3c",
                        relief="raised",
                        borderwidth=3)

        style.map("Danger.TButton",
                  background=[('active', '#c0392b'), ('pressed', '#922b21')],
                  foreground=[('active', 'white')],
                  relief=[('active', 'sunken'), ('pressed', 'sunken')])

        # Success button style for additional visibility
        style.configure("Success.TButton",
                        font=("Segoe UI", 14, "bold"),
                        padding=12,
                        foreground="white",
                        background="#27ae60",
                        bordercolor="#27ae60",
                        relief="raised",
                        borderwidth=3)

        style.map("Success.TButton",
                  background=[('active', '#219653'), ('pressed', '#1e8449')],
                  foreground=[('active', 'white')],
                  relief=[('active', 'sunken'), ('pressed', 'sunken')])

        # Entry style
        style.configure("Modern.TEntry",
                        font=("Segoe UI", 12),
                        padding=8,
                        bordercolor="#bdc3c7",
                        lightcolor="#bdc3c7",
                        darkcolor="#bdc3c7",
                        relief="flat",
                        fieldbackground="white")

        # Label style
        style.configure("Modern.TLabel",
                        font=("Segoe UI", 11),
                        background="#f0f0f0",
                        foreground="#2c3e50")

        # Treeview style
        style.configure("Treeview",
                        font=("Segoe UI", 11),
                        rowheight=30,
                        background="white",
                        fieldbackground="white",
                        foreground="#2c3e50")

        style.configure("Treeview.Heading",
                        font=("Segoe UI", 11, "bold"),
                        background="#3498db",
                        foreground="white",
                        relief="flat")

        style.map("Treeview.Heading",
                  background=[('active', '#2980b9')])

    def create_main_page(self):
        """Create the main page of the application"""
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create main frame
        main_frame = ttk.Frame(self.root, style="Main.TFrame")
        main_frame.pack(expand=True, fill="both", padx=50, pady=50)

        # Header with logo and title
        header_frame = ttk.Frame(main_frame, style="Main.TFrame")
        header_frame.pack(pady=(0, 40))

        title_frame = ttk.Frame(header_frame, style="Main.TFrame")
        title_frame.pack(side="left", padx=20)

        ttk.Label(title_frame, text="Smart Attendance System",
                  style="Title.TLabel").pack()
        ttk.Label(title_frame, text="Face Recognition Based Attendance Management",
                  style="Modern.TLabel").pack()

        # Buttons container
        buttons_frame = ttk.Frame(main_frame, style="Main.TFrame")
        buttons_frame.pack(expand=True)

        # Buttons with improved visibility
        login_btn = ttk.Button(buttons_frame,
                               text="Login",
                               style="Primary.TButton",
                               command=self.create_login_page)
        login_btn.pack(pady=20, ipadx=50, ipady=15)

        register_btn = ttk.Button(buttons_frame,
                                  text="Register New User",
                                  style="Success.TButton",  # Changed to success style for better distinction
                                  command=self.create_register_page)
        register_btn.pack(pady=20, ipadx=30, ipady=15)

        # Footer
        footer_frame = ttk.Frame(main_frame, style="Main.TFrame")
        footer_frame.pack(side="bottom", pady=20)

        ttk.Label(footer_frame,
                  text="© 2025 Smart Attendance System | Version 2.0",
                  style="Modern.TLabel").pack()

    def create_register_page(self):
        """Create the user registration page"""
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Main container
        main_frame = ttk.Frame(self.root, style="Main.TFrame")
        main_frame.pack(expand=True, fill="both", padx=30, pady=30)

        # Header
        header_frame = ttk.Frame(main_frame, style="Main.TFrame")
        header_frame.pack(fill="x", pady=(0, 30))

        ttk.Button(header_frame, text="← Back",
                   style="Secondary.TButton",
                   command=self.create_main_page).pack(side="left")

        ttk.Label(header_frame, text="Register New User",
                  style="Title.TLabel").pack(side="left", padx=20)

        # Form container
        form_frame = ttk.Frame(main_frame, style="Main.TFrame")
        form_frame.pack(fill="both", expand=True)

        # Left side - form fields
        left_frame = ttk.Frame(form_frame, style="Main.TFrame")
        left_frame.pack(side="left", fill="both", expand=True, padx=20)

        # Form fields
        self.name_var = tk.StringVar()
        self.enrollment_var = tk.StringVar()
        self.college_var = tk.StringVar()
        self.class_var = tk.StringVar()
        self.section_var = tk.StringVar()

        fields = [
            ("Full Name:", self.name_var),
            ("Enrollment Number:", self.enrollment_var),
            ("College/Institution:", self.college_var),
            ("Class/Department:", self.class_var),
            ("Section/Batch:", self.section_var)
        ]

        for label_text, var in fields:
            field_frame = ttk.Frame(left_frame, style="Main.TFrame")
            field_frame.pack(pady=10, fill="x")

            ttk.Label(field_frame, text=label_text,
                      style="Modern.TLabel").pack(side="left", padx=5)

            ttk.Entry(field_frame, textvariable=var,
                      style="Modern.TEntry").pack(side="right", expand=True, fill="x", padx=5)

        # Right side - face capture
        right_frame = ttk.Frame(form_frame, style="Main.TFrame")
        right_frame.pack(side="right", fill="both", expand=True, padx=20)

        # Face capture container
        face_frame = ttk.LabelFrame(right_frame, text="Face Capture",
                                    style="Modern.TLabel")
        face_frame.pack(fill="both", expand=True, pady=10)

        self.face_label = ttk.Label(face_frame,
                                    text="No face captured yet",
                                    style="Modern.TLabel")
        self.face_label.pack(expand=True, pady=20)

        # Buttons with improved visibility
        btn_frame = ttk.Frame(right_frame, style="Main.TFrame")
        btn_frame.pack(fill="x", pady=20)

        ttk.Button(btn_frame, text="Capture Face",
                   style="Primary.TButton",
                   command=self.capture_face).pack(side="left", padx=5, ipadx=10, ipady=5)

        ttk.Button(btn_frame, text="Register",
                   style="Success.TButton",
                   command=self.register).pack(side="left", padx=5, ipadx=20, ipady=5)

        ttk.Button(btn_frame, text="Cancel",
                   style="Danger.TButton",
                   command=self.create_main_page).pack(side="right", padx=5, ipadx=20, ipady=5)

    def capture_face(self):
        """Capture face using webcam"""
        cap = cv2.VideoCapture(0)

        # Create a new window for face capture
        capture_window = tk.Toplevel(self.root)
        capture_window.title("Face Capture")
        capture_window.geometry("800x600")

        # Video frame
        video_frame = ttk.Frame(capture_window)
        video_frame.pack(expand=True, fill="both", padx=20, pady=20)

        video_label = ttk.Label(video_frame)
        video_label.pack(expand=True)

        # Instructions
        ttk.Label(capture_window,
                  text="Position your face in the frame and press 'Capture' when ready",
                  style="Modern.TLabel").pack(pady=10)

        # Capture button with improved visibility
        btn_frame = ttk.Frame(capture_window)
        btn_frame.pack(pady=10)

        def on_capture():
            nonlocal cap
            ret, frame = cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

                if len(faces) > 0:
                    x, y, w, h = faces[0]
                    face = gray[y:y + h, x:x + w]
                    self.face_template = cv2.resize(face, (100, 100))

                    # Display captured face in the main form
                    img = Image.fromarray(self.face_template)
                    img = img.resize((200, 200), Image.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    self.face_label.configure(image=photo)
                    self.face_label.image = photo
                    self.face_label.configure(text="")

                    capture_window.destroy()
                    cap.release()
                else:
                    messagebox.showerror("Error", "No face detected. Please try again.")

        ttk.Button(btn_frame, text="Capture",
                   style="Primary.TButton",
                   command=on_capture).pack(side="left", padx=10, ipadx=20, ipady=5)

        ttk.Button(btn_frame, text="Cancel",
                   style="Danger.TButton",
                   command=lambda: [capture_window.destroy(), cap.release()]).pack(side="right", padx=10, ipadx=20, ipady=5)

        # Function to update video feed
        def update_video():
            ret, frame = cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                img = img.resize((640, 480), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)

                video_label.configure(image=photo)
                video_label.image = photo

            video_label.after(10, update_video)

        update_video()

    def register(self):
        """Register a new user"""
        if not all([
            self.name_var.get(),
            self.enrollment_var.get(),
            self.college_var.get(),
            self.class_var.get(),
            self.section_var.get(),
            hasattr(self, 'face_template')
        ]):
            messagebox.showerror("Error", "Please fill all fields and capture a face")
            return

        # Convert face template to bytes
        face_template = cv2.imencode('.jpg', self.face_template)[1].tobytes()

        # Register user in database
        if self.db.register_user(
                self.name_var.get(),
                self.enrollment_var.get(),
                self.college_var.get(),
                self.class_var.get(),
                self.section_var.get(),
                face_template
        ):
            messagebox.showinfo("Success", "Registration successful!")
            self.create_main_page()
        else:
            messagebox.showerror("Error", "Registration failed. Enrollment number might already exist.")

    def create_login_page(self):
        """Create the login page"""
        for widget in self.root.winfo_children():
            widget.destroy()

        # Main container
        main_frame = ttk.Frame(self.root, style="Main.TFrame")
        main_frame.pack(expand=True, fill="both", padx=50, pady=50)

        # Header
        header_frame = ttk.Frame(main_frame, style="Main.TFrame")
        header_frame.pack(fill="x", pady=(0, 30))

        ttk.Button(header_frame, text="← Back",
                   style="Secondary.TButton",
                   command=self.create_main_page).pack(side="left")

        ttk.Label(header_frame, text="User Login",
                  style="Title.TLabel").pack(side="left", padx=20)

        # Login form
        form_frame = ttk.Frame(main_frame, style="Main.TFrame")
        form_frame.pack(expand=True, fill="both")

        # Center the form
        center_frame = ttk.Frame(form_frame, style="Main.TFrame")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.login_name_var = tk.StringVar()
        self.login_enrollment_var = tk.StringVar()

        fields = [
            ("Name:", self.login_name_var),
            ("Enrollment Number:", self.login_enrollment_var)
        ]

        for label_text, var in fields:
            field_frame = ttk.Frame(center_frame, style="Main.TFrame")
            field_frame.pack(pady=15, fill="x")

            ttk.Label(field_frame, text=label_text,
                      style="Modern.TLabel").pack(side="left", padx=5)

            ttk.Entry(field_frame, textvariable=var,
                      style="Modern.TEntry", width=30).pack(side="right", padx=5)

        # Buttons with improved visibility
        btn_frame = ttk.Frame(center_frame, style="Main.TFrame")
        btn_frame.pack(pady=30)

        ttk.Button(btn_frame, text="Login",
                   style="Primary.TButton",
                   command=self.login).pack(side="left", padx=10, ipadx=20, ipady=5)

        ttk.Button(btn_frame, text="Cancel",
                   style="Danger.TButton",
                   command=self.create_main_page).pack(side="right", padx=10, ipadx=20, ipady=5)

    def login(self):
        """Verify user login"""
        result = self.db.verify_login(self.login_name_var.get(), self.login_enrollment_var.get())
        if result:
            self.user_id = result[0]
            face_array = np.frombuffer(result[1], dtype=np.uint8)
            self.stored_template = cv2.imdecode(face_array, cv2.IMREAD_GRAYSCALE)
            self.stored_template = cv2.resize(self.stored_template, (100, 100))
            self.create_options_page()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def create_options_page(self):
        """Create the options page after successful login"""
        for widget in self.root.winfo_children():
            widget.destroy()

        # Main container
        main_frame = ttk.Frame(self.root, style="Main.TFrame")
        main_frame.pack(expand=True, fill="both", padx=50, pady=50)

        # Header
        header_frame = ttk.Frame(main_frame, style="Main.TFrame")
        header_frame.pack(fill="x", pady=(0, 20))

        user_info = self.db.get_user_info(self.user_id)

        ttk.Label(header_frame, text=f"Welcome, {user_info[0]}",
                  style="Title.TLabel").pack(side="left")

        ttk.Button(header_frame, text="Logout",
                   style="Danger.TButton",
                   command=self.create_main_page).pack(side="right", ipadx=10, ipady=5)

        # User info
        info_frame = ttk.Frame(main_frame, style="Main.TFrame")
        info_frame.pack(fill="x", pady=20)

        ttk.Label(info_frame,
                  text=f"Enrollment: {user_info[1]} | {user_info[2]} | {user_info[3]} - {user_info[4]}",
                  style="Modern.TLabel").pack()

        # Buttons with improved visibility
        btn_frame = ttk.Frame(main_frame, style="Main.TFrame")
        btn_frame.pack(expand=True)

        ttk.Button(btn_frame, text="Take Attendance",
                   style="Primary.TButton",
                   command=self.take_attendance).pack(pady=15, ipadx=30, ipady=15)

        ttk.Button(btn_frame, text="View Attendance",
                   style="Success.TButton",  # Changed to success style for better visibility
                   command=self.view_attendance).pack(pady=15, ipadx=30, ipady=15)

    def take_attendance(self):
        """Take attendance using face recognition"""
        attendance_window = tk.Toplevel(self.root)
        attendance_window.title("Take Attendance")
        attendance_window.geometry("1000x700")

        # Video frame
        video_frame = ttk.Frame(attendance_window)
        video_frame.pack(expand=True, fill="both", padx=20, pady=20)

        self.video_label = ttk.Label(video_frame)
        self.video_label.pack(expand=True)

        # Status frame
        status_frame = ttk.Frame(attendance_window)
        status_frame.pack(fill="x", padx=20, pady=10)

        self.status_label = ttk.Label(status_frame,
                                      text="Position your face in the frame and click 'Mark Attendance'",
                                      style="Modern.TLabel")
        self.status_label.pack(side="left")

        # Buttons with improved visibility
        btn_frame = ttk.Frame(attendance_window)
        btn_frame.pack(fill="x", padx=20, pady=20)

        ttk.Button(btn_frame, text="Mark Attendance",
                   style="Primary.TButton",
                   command=lambda: self.capture_and_mark_attendance(attendance_window)).pack(side="left", padx=10, ipadx=10, ipady=5)

        ttk.Button(btn_frame, text="Close",
                   style="Danger.TButton",
                   command=attendance_window.destroy).pack(side="right", padx=10, ipadx=20, ipady=5)

        # Start video capture
        self.cap = cv2.VideoCapture(0)
        self.update_video_feed()

        # Store window reference
        self.attendance_window = attendance_window

    def update_video_feed(self):
        """Update the video feed in real-time"""
        ret, frame = self.cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = img.resize((800, 600), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)

            self.video_label.configure(image=photo)
            self.video_label.image = photo

            self.video_label.after(10, self.update_video_feed)

    def capture_and_mark_attendance(self, window):
        """Capture face and mark attendance"""
        ret, frame = self.cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

            if len(faces) > 0:
                x, y, w, h = faces[0]
                face = gray[y:y + h, x:x + w]
                face = cv2.resize(face, (100, 100))

                # Compare with stored template
                diff = cv2.absdiff(face, self.stored_template)
                if np.mean(diff) < 50:  # Threshold for similarity
                    # Get user info and mark attendance
                    user_info = self.db.get_user_info(self.user_id)
                    if user_info:
                        name, enrollment = user_info[0], user_info[1]
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        # Update attendance in database
                        success, message = self.db.mark_attendance(self.user_id, current_time)
                        if success:
                            self.status_label.config(text="Attendance marked successfully!")

                            # Show success message in a dialog
                            success_window = tk.Toplevel(window)
                            success_window.title("Success")
                            success_window.geometry("500x300")

                            ttk.Label(success_window,
                                      text="Attendance Marked Successfully!",
                                      style="Title.TLabel").pack(pady=20)

                            ttk.Label(success_window,
                                      text=f"Name: {name}\nEnrollment: {enrollment}\nTime: {current_time}",
                                      style="Modern.TLabel").pack(pady=10)

                            ttk.Button(success_window,
                                       text="OK",
                                       style="Success.TButton",
                                       command=lambda: [success_window.destroy(), window.destroy()]).pack(pady=20)

                            self.cap.release()
                            self.view_attendance()  # Show updated attendance
                        else:
                            messagebox.showwarning("Warning", message)
                else:
                    messagebox.showerror("Error", "Face not recognized. Please try again.")
            else:
                messagebox.showerror("Error", "No face detected. Please try again.")

    def view_attendance(self):
        """View attendance records"""
        records = self.db.get_attendance(self.user_id)

        attendance_window = tk.Toplevel(self.root)
        attendance_window.title("Attendance Records")
        attendance_window.geometry("1200x700")

        # Main container
        main_frame = ttk.Frame(attendance_window)
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Header
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill="x", pady=(0, 20))

        ttk.Label(header_frame,
                  text="Your Attendance History",
                  style="Title.TLabel").pack(side="left")

        # Treeview with scrollbars
        tree_frame = ttk.Frame(main_frame)
        tree_frame.pack(expand=True, fill="both")

        tree = ttk.Treeview(tree_frame,
                            columns=("Name", "Enrollment", "College", "Class", "Section", "Date", "Time", "Status"),
                            show="headings")

        # Configure columns
        for col in tree["columns"]:
            tree.heading(col, text=col)
            tree.column(col, width=140, anchor="center")

        # Add scrollbars
        y_scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        x_scrollbar = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)

        # Pack widgets
        tree.pack(side="left", fill="both", expand=True)
        y_scrollbar.pack(side="right", fill="y")
        x_scrollbar.pack(side="bottom", fill="x")

        # Add records to treeview
        for record in records:
            tree.insert("", "end", values=record)

        # Summary frame
        summary_frame = ttk.Frame(main_frame)
        summary_frame.pack(fill="x", pady=(20, 0))

        # Calculate attendance statistics
        total_days = len(records)
        present_days = sum(1 for record in records if record[7] == "Present")
        attendance_percentage = (present_days / total_days * 100) if total_days > 0 else 0

        # Display statistics
        ttk.Label(summary_frame,
                  text=f"Total Days: {total_days} | Present Days: {present_days} | Attendance: {attendance_percentage:.1f}%",
                  style="Modern.TLabel").pack(side="left")

        # Export button with improved visibility
        ttk.Button(summary_frame, text="Export to Excel",
                   style="Secondary.TButton").pack(side="right", padx=10, ipadx=10, ipady=5)

        # Close button with improved visibility
        ttk.Button(summary_frame, text="Close",
                   style="Danger.TButton",
                   command=attendance_window.destroy).pack(side="right", padx=10, ipadx=20, ipady=5)

    def run(self):
        """Run the application"""
        self.root.mainloop()


if __name__ == "__main__":
    app = AttendanceSystem()
    app.run()