#Author: Avery Cordle
from bird import Bird

bird_list = (
    Bird("Black-chinned Hummingbird", "White/green bodies and black/purple heads", "Nectar", "These birds can be found on the North American west coast and have average heart beats of 480 beats per minute."),
    #https://www.allaboutbirds.org/guide/Black-chinned_Hummingbird/overview
    Bird("Carolina Chickadee", "Yellow bodies with white and black heads and wings", "Insects", "These birds are native to the southeast United States and can hybridize with Black-capped chickadees."),
    #https://www.allaboutbirds.org/guide/Carolina_Chickadee/overview
    Bird("Peregrine Falcon", "White/gray striped bodies with gray head and wings", "Other birds", "These birds are prized hunting birds and can fly downwards at speed of 200 mph."),
    #https://www.allaboutbirds.org/guide/Peregrine_Falcon/overview
    Bird("American Goldfinch", "Yellow bodies with black wings and forehead", "Seeds", "These birds almost exclusively live in the United States and are very strict vegtarians, only eating the occasionaly insect (when desperate.)")
    #https://www.allaboutbirds.org/guide/American_Goldfinch/overview
)

print("Bird Program!")

while True:
    command = input("(L)ist all birds, get a birds (D)etails, or (Q)uit: ").lower().strip()

    if command == "q":
        break
    if command == "l":
        for bird in bird_list:
            bird.display()
    elif command == "d":
        bird_names = input("Enter bird name: ").strip()
        print("Bird that matches this name:")
        for bird in bird_list:
            if bird.is_match(bird_names):
                bird.display()
    else: 
        print("Invalid Command")   

print("Goodbye")