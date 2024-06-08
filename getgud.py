import random
import tkinter as tk
from PIL import Image, ImageTk

FPSTips = ["Know the Map", "Practice Aim", "Use Cover", "Manage Reloads", "Communicate", "Watch Your Flanks", "Use Sound", "Adapt Your Loadout", "Stay Mobile", "Stay Calm", "Learn from Mistakes", "Play Regularly", "Control Recoil", "Master Movement", "Pre-aim Corners", "Utilize Grenades", "Check Your Radar", "Stay Aware of Objectives", "Study Enemy Patterns", "Adjust Sensitivity Settings", "Customize Controls", "Stay Patient", "Keep a Positive Attitude", "Enjoy the Game"]
StealthTips = ["Stay Hidden", "Use Distractions", "Plan Your Routes", "Silent Takedowns", "Avoid Line of Sight", "Use Shadows", "Listen for Enemy Movement", "Hacking and Lockpicking", "Patience is Key", "Learn Enemy Patterns", "Hide Bodies", "Use Gadgets Wisely"]
SurvivalTips = ["Gather Resources", "Build Shelter", "Manage Hunger and Thirst", "Craft Tools and Weapons", "Avoid Dangerous Areas", "Hunt or Forage for Food", "Stay Warm/Cool", "Watch Out for Wildlife", "Be Prepared for Emergencies", "Cooperate with Others", "Explore the Environment", "Upgrade Your Gear"]
SportTips = ["Master Controls", "Learn Plays and Strategies", "Practice Timing", "Understand Player Roles", "Utilize Teamwork", "Study Opponent Strategies", "Adapt to Different Playstyles", "Maintain Fitness", "Watch Tutorials", "Analyze Matches", "Stay Calm Under Pressure", "Celebrate Successes"]
MOBATips = ["Farm Creeps", "Control Objectives", "Communicate with Teammates", "Coordinate Ganks", "Ward Important Areas", "Map Awareness", "Learn Hero Abilities", "Counter Enemy Picks", "Manage Resources", "Adjust Builds", "Be Flexible in Roles", "Time Ultimates Wisely"]
DrivingTips = ["Master Cornering", "Manage Speed", "Use Boosts Strategically", "Watch Out for Obstacles", "Stay on Track", "Study Track Layouts", "Learn Braking Techniques", "Avoid Collisions", "Upgrade Vehicles", "Tune Handling", "Practice Drifting", "Compete Fairly"]

class GetGud:
    def __init__(self, root):
        self.root = root
        self.root.title("Get Gud")
        self.root.geometry("400x400")
        root.config(bg='#3159a3')
        self.genre = ""
        self.first_page()

    def first_page(self):
        self.clear_page()
        
        label = tk.Label(self.root, text="Choose your game category", font=("Calibri", 24), bg='#dcecfa', fg='#7092be')
        label.pack(pady=20)
        
        buttons = [
            ("FPS", self.Generate_FPS_tip),
            ("Stealth", self.Generate_Stealth_Tip),
            ("Sport", self.Generate_Sport_Tip),
            ("MOBA", self.Generate_MOBA_Tip),
            ("Survival", self.Generate_Survival_Tip),
            ("Driving", self.Generate_Driving_Tip)
        ]
        
        for text, command in buttons:
            button = tk.Button(self.root, text=text, fg="#99d9ea", command=command)
            button.pack()

    def second_page(self):
        self.clear_page()
        
        self.back_button = tk.Button(self.root, text="Back", fg="#99d9ea", command=self.first_page)
        self.back_button.pack(pady=10)
        
        self.tip_label = tk.Label(self.root, font=("Calibri", 14), bg='#dcecfa', fg='#7092be')
        self.tip_label.pack(pady=20)
        
        self.generate_button = tk.Button(self.root, text="Generate Tip", fg="#99d9ea", command=self.Give_Tip)
        self.generate_button.pack(pady=10)

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)
        
        self.Give_Tip()
        self.display_image()

    def clear_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def display_image(self):
        genre_images = {
            "FPS": "fps.jpeg",
            "Stealth": "stealth.jpg",
            "Sport": "sports.jpg",
            "Survival": "survival.png",
            "MOBA": "moba.png",
            "Driving": "driving.png"
        }

        image_path = genre_images.get(self.genre, "")
        if image_path:
            image = Image.open(image_path)
            image = image.resize((200, 200))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def Generate_FPS_tip(self):
        self.genre = "FPS"
        self.second_page()

    def Generate_Stealth_Tip(self):
        self.genre = "Stealth"
        self.second_page()

    def Generate_Sport_Tip(self):
        self.genre = "Sport"
        self.second_page()

    def Generate_MOBA_Tip(self):
        self.genre = "MOBA"
        self.second_page()

    def Generate_Survival_Tip(self):
        self.genre = "Survival"
        self.second_page()

    def Generate_Driving_Tip(self):
        self.genre = "Driving"
        self.second_page()

    def Give_Tip(self):
        tips_dict = {
            "FPS": FPSTips,
            "Stealth": StealthTips,
            "Sport": SportTips,
            "Survival": SurvivalTips,
            "MOBA": MOBATips,
            "Driving": DrivingTips
        }
        
        random_text = random.choice(tips_dict.get(self.genre, []))
        self.tip_label.config(text=random_text)
        print(random_text)

root = tk.Tk()
getGud = GetGud(root)
root.mainloop()
