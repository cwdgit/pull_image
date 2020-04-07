

import os



def pull_image(image_list):
    
    for name in image_list:
        print(name)
        os.system("docker pull {}".format(name))



def push_image(imagelist):
    for name in imagelist:
        print(name)
	image_name = name[name.rfind('/'):name.rfind(':')]
        os.system("docker push 192.168.16.104:31104/aoip{}:v2".format(image_name))
    

def image_tag(imagelist):
    
    
    for name in imagelist:
        print(name)

        image_name = name[name.rfind('/'):name.rfind(':')]
        cmd_tag = 'docker tag {} 192.168.16.104:31104/aoip{}:v2'.format(name,image_name)
        os.system(cmd_tag)
    
        


    
        
    


def main():
    imagelist=[]
    with open('aoip_imagelist','r') as f:
        for line in f:
            new_line=line.strip()
            imagelist.append(new_line)
    #pull_image(imagelist)
    #image_tag(imagelist)
    push_image(imagelist)    
    
            

    
    
    

    


if __name__ == "__main__":
    main()







