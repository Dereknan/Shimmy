#Problems








import random




import tkinter as tk

FPSTips=["Know the Map", "Practice Aim", "Use Cover", "Manage Reloads", "Communicate", "Watch Your Flanks", "Use Sound", "Adapt Your Loadout", "Stay Mobile", "Stay Calm", "Learn from Mistakes", "Play Regularly","Control Recoil", "Master Movement", "Pre-aim Corners", "Utilize Grenades", "Check Your Radar", "Stay Aware of Objectives", "Study Enemy Patterns", "Adjust Sensitivity Settings", "Customize Controls", "Stay Patient", "Keep a Positive Attitude", "Enjoy the Game"]
StealthTips=["Stay Hidden", "Use Distractions", "Plan Your Routes", "Silent Takedowns", "Avoid Line of Sight", "Use Shadows", "Listen for Enemy Movement", "Hacking and Lockpicking", "Patience is Key", "Learn Enemy Patterns", "Hide Bodies", "Use Gadgets Wisely"]
SurvivalTips=["Gather Resources", "Build Shelter", "Manage Hunger and Thirst", "Craft Tools and Weapons", "Avoid Dangerous Areas", "Hunt or Forage for Food", "Stay Warm/Cool", "Watch Out for Wildlife", "Be Prepared for Emergencies", "Cooperate with Others", "Explore the Environment", "Upgrade Your Gear"]
SportTips=["Master Controls", "Learn Plays and Strategies", "Practice Timing", "Understand Player Roles", "Utilize Teamwork", "Study Opponent Strategies", "Adapt to Different Playstyles", "Maintain Fitness", "Watch Tutorials", "Analyze Matches", "Stay Calm Under Pressure", "Celebrate Successes"]
MOBATips=["Farm Creeps", "Control Objectives", "Communicate with Teammates", "Coordinate Ganks", "Ward Important Areas", "Map Awareness", "Learn Hero Abilities", "Counter Enemy Picks", "Manage Resources", "Adjust Builds", "Be Flexible in Roles", "Time Ultimates Wisely"]
DrivingTips=["Master Cornering", "Manage Speed", "Use Boosts Strategically", "Watch Out for Obstacles", "Stay on Track", "Study Track Layouts", "Learn Braking Techniques", "Avoid Collisions", "Upgrade Vehicles", "Tune Handling", "Practice Drifting", "Compete Fairly"]





class GetGud:
    def __init__(self,root):
        self.root = root
        self.root.title("Get Gud") 
        self.root.geometry("400x300")
        root.config(bg='#3159a3')
        self.genre = ""
        self.first_page()


    def delete_buttons(self):
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
        self.button5.destroy()
        self.button6.destroy()

    def delete_dropdowns(self):
        self.delete_dropdowns
    
    
    
    def first_page(self):
        label = tk.Label(root, text = "Choose your game category",
        font = ("Calibri 24"), bg ='#dcecfa', fg = '#7092be' )
        label.pack(pady =20)

        self.button1 = tk.Button(root, text ="FPS", fg = "#99d9ea", command = self.Generate_FPS_tip)
        self.button2 = tk.Button(root, text ="Stealth", fg = "#99d9ea", command = self.Generate_Stealth_Tip)
        self.button3 = tk.Button(root, text ="Sport", fg = "#99d9ea", command = self.Generate_Sport_Tip)
        self.button4 = tk.Button(root, text ="MOBA", fg = "#99d9ea", command = self.Generate_MOBA_Tip)
        self.button5 = tk.Button(root, text ="Survival", fg = "#99d9ea", command = self.Generate_Survival_Tip)
        self.button6 = tk.Button(root, text ="Driving", fg = "#99d9ea", command = self.Generate_Driving_Tip)
        
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button5.pack()
        self.button6.pack()

    def second_page(self):
        
        self.button7 = tk.Button(root, text ="Generate Tip", fg = "#99d9ea", command = self.Give_Tip)
        self.button7.pack()
        self.delete_buttons()
        self.selected_option = tk.StringVar()
        random_texts = random.choice(FPSTips)
        self.selected_option.set(random_texts)
        label = tk.Label(root, textvariable = self.selected_option)
        
        print("Tip given "+random_texts)
        #font = ("Calibri 10"), bg ='#dcecfa', fg = ('#7092be' )
        label.pack(pady =20)
        
    def button_press(self):
        self.button1.destroy
        self.button2.destroy
        self.button3.destroy
        self.button4.destroy
        self.button5.destroy
        self.button6.destroy
    
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
        if self.genre == "FPS":
            random_text = random.choice(FPSTips)
        if self.genre == "Stealth":
            random_text = random.choice(StealthTips)
        if self.genre == "Sport":
            random_text = random.choice(SportTips)
        if self.genre == "Survival":
            random_text = random.choice(SurvivalTips)
        if self.genre == "MOBA":
            random_text = random.choice(MOBATips)
        if self.genre == "Driving":
            random_text = random.choice(DrivingTips)
        
        self.selected_option.set(random_text)
        print(random_text)
    
    




root = tk.Tk()
getGud=GetGud(root)
root.mainloop()



