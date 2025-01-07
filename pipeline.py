
import cmd, os
import json
import shutil
from sys import platform


class Pipe(cmd.Cmd):
    prompt = "waldo: "
    intro = "Welcome to the Waldo pipeline!"

    def do_predict(self, cut_technique=False, scale_technique=False, analytics=False, clean=False):

        trained_model_exists = os.path.exists("best.pt")

        print("Predicting the location of Waldo in the image")

        if not clean:
            errorCode = shutil.rmtree("output/", ignore_errors=True)

        if not trained_model_exists:
            print("Model not found. Please train the model first with waldo: train")
            return
        
        if not cut_technique:
            print("Cutting the image")
            # call cut_image.py 
            exit_code = os.system("python cut_images.py")
            if exit_code != 0:
                print("Image cutting failed")
                return
            print("Image cut successfully")

            print("predicting")

            # call cut_predict.py
            exit_code = os.system("python cut_predict.py")
            if exit_code != 0:
                print("Prediction failed")
                return
            print("Prediction successful")

        if not scale_technique:
            print("Scaling the image")

        if not analytics:
            print("Outputting analytics")

            match(platform):
                case "linux" | "linux2":
                    os.system("xdg-open report.html")
                case "darwin":
                    os.system("open report.html")
                case "win32":
                    os.system("start report.html")
                case _:
                    print("Unsupported platform")
                
    
    def help_predict(self):
        print("Predict the location of Waldo in the image using the trained model, set cut_technique to True to cut the image into smaller images, set scale_technique to True to scale the image to 256x256, set analytics to True to show analytics output")

    def do_train(self):
        print("Training the model")

        # check if dataset images and labels exist
        if not os.path.exists("dataset/images") or not os.path.exists("dataset/labels"):
            print("Dataset images or labels not found. Please add them to the dataset folder")
            return

        # Call train.py script check exit Code
        exit_code = os.system("python train.py")
        if exit_code != 0:
            print("Model training failed")
            return

        print("Model trained successfully")

    def help_train(self):
        print("Train a model to detect Waldo in images, a dataset is required at dataset/images and dataset/labels")

if __name__ == "__main__":
    Pipe().cmdloop()
