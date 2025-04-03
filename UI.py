import ttkthemes
import tkinter
from tkinter import *
from tkinter import ttk

from ttkthemes.themed_tk import ThemedTk

from openai_API import processInput


# The whole UI
def startUI():

    # Creating functions for buttons
    def submittingData():
        promptUserData = f"I am building a fitness and diet planner. Based on the following user info: Age: {userAge.get()}, Weight: {userWeight.get()}, Height: {userHeight.get()}, Gender: {userGender.get()}, Activity level: {userActivLevel.get()}, Goal: {userGoal.get()}, Available workout days per week: {userWorkDays.get()}. I want you to calculate recommended daily calories and split them into macronutrients (protein, carbs, fats) with grams, provide a 1-day sample meal plan (breakfast, lunch, dinner, snack) with rough estimates, and create a weekly workout plan based on the available days. Each workout should target different muscle groups and include links to YouTube videos demonstrating the exercises. Keep the tone encouraging and easy to understand, as if you're coaching a beginner."
        # popping a new window to show the prompt
        plan_window = tkinter.Toplevel(root)
        plan_window.title("The plan")
        plan_window.geometry("1080x720")

        plan_text = tkinter.Text(plan_window)
        plan_text.insert(1.0, processInput(promptUserData))
        plan_text['state'] = 'disabled'
        plan_text.pack(fill = 'x')


    root = Tk()
    root.title("Fitness planner")
    root.geometry("300x450")

    # variables to store values entered by user in input boxes
    userAge = tkinter.StringVar()
    userWeight = tkinter.StringVar()
    userHeight = tkinter.StringVar()
    userGender = tkinter.StringVar()
    userActivLevel = tkinter.StringVar()
    userGoal = tkinter.StringVar()
    userWorkDays = tkinter.StringVar()

    # creating the data entry frame
    frmDataEntry = ttk.Frame(root)
    frmDataEntry.pack(padx=10, pady=10, fill=tkinter.X)

    # Here is where we get the user's Age
    ageLabel = ttk.Label(frmDataEntry, text="Age")
    ageLabel.pack(fill = 'x')

    ageEntry = ttk.Entry(frmDataEntry, textvariable=userAge)
    ageEntry.pack(fill = 'x')

    # This is where we take the user's weight
    weightLabel = ttk.Label(frmDataEntry, text='Weight (in kg)')
    weightLabel.pack(fill="x")

    weightEntry = ttk.Entry(frmDataEntry, textvariable=userWeight)
    weightEntry.pack(fill="x")

    # Here is where we take the user's height
    heightLabel = ttk.Label(frmDataEntry, text = "Height (in cm)")
    heightLabel.pack(fill = "x")

    heightEntry = ttk.Entry(frmDataEntry, textvariable=userHeight)
    heightEntry.pack(fill="x")

    # Here is where we take the user's gender
    genderLabel = ttk.Label(frmDataEntry, text='Gender')
    genderLabel.pack(fill = 'x')

    genderCombo = ttk.Combobox(frmDataEntry, textvariable=userGender)
    genderCombo['values'] = ["Male", "Female"]
    genderCombo['state'] = 'readonly'
    genderCombo.pack(fill = 'x')

    # Getting user activity level
    activLabel = ttk.Label(frmDataEntry, text= 'Activity level')
    activLabel.pack(fill='x')

    activCombo = ttk.Combobox(frmDataEntry, textvariable=userActivLevel)
    activCombo['values'] = ['Sedentary - less than 3000 steps a day', 'Lightly active - Between 4000 and 7000 steps a day', 'Moderately active - Between 7000 and 10000 steps a day', 'Very active - 10000+ steps a day']
    activCombo['state'] = 'readonly'
    activCombo.pack(fill= 'x')

    # Getting user goal
    goalLabel = ttk.Label(frmDataEntry, text= 'Goal')
    goalLabel.pack(fill = 'x')

    goalCombo = ttk.Combobox(frmDataEntry, textvariable=userGoal)
    goalCombo['values'] = ['Lose fat', 'Gain muscle', 'Maintain', 'Recomp (lose fat, gain muscle)']
    goalCombo['state'] = 'readonly'
    goalCombo.pack(fill = 'x')

    # Getting user workout days
    workDaysLabel = ttk.Label(frmDataEntry, text= 'How many days available a week')
    workDaysLabel.pack(fill = 'x')

    workDaysCombo = ttk.Combobox(frmDataEntry, textvariable=userWorkDays)
    workDaysCombo['values'] = ['5 days', '4 days', '3 days']
    workDaysCombo['state'] = 'readonly'
    workDaysCombo.pack(fill = 'x')

    # Button to submit data
    submitButton = ttk.Button(frmDataEntry, text="Submit", command=submittingData)
    submitButton.pack(pady = 6)

    root.mainloop()

