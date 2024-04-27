from tqdm import tqdm
import time



def barre(total):
    
    for i in tqdm(range(total), desc="Progression"):
        time.sleep(0.1)  

if __name__ == "__main__":
    barre()
