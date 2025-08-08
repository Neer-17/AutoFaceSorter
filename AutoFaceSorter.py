import os
import face_recognition

def face_sort(directory):
    list_faces = []
    list_others = []
    for file in os.listdir(directory):
        if file.endswith('png') or file.endswith('jpg') or file.endswith('jpeg'):
            file_path = os.path.join(directory,file)
            sample_img = face_recognition.load_image_file(file_path)
            try:
                person = face_recognition.face_encodings(sample_img)[0]
                list_faces.append(file_path)
            except IndexError as i :
                list_others.append(file)
    
    list_faces_1 = list_faces.copy()
    k = 0
    try:
        for i in range(0,len(list_faces)):
            i=0
            
            #print(f"\nUsing {list_faces[i]} as sample_img_load for person_{k}")
            person_dir = os.path.join(directory,f"person_{k}")
            if not os.path.exists(person_dir):
                os.makedirs(person_dir)
            sample_img_load = face_recognition.load_image_file(list_faces[i])
            sample_face = face_recognition.face_encodings(sample_img_load)[0]
            to_remove = []
            for j in list_faces_1:
              #print(f"\nnow comparing {list_faces[i]} with {j}")
                test_img = face_recognition.load_image_file(j)
                test_face = face_recognition.face_encodings(test_img)[0]
                result = face_recognition.compare_faces([sample_face],test_face)
                if result[0]:
                    os.rename(j,os.path.join(person_dir,os.path.basename(j)))
                    to_remove.append(j)
            for item in to_remove:
                list_faces_1.remove(item)
                list_faces.remove(item)
            print(list_faces)
            k+=1
            
    except IndexError as e:
        print("Sorting complete.")
        return
                
address = r'' #Enter Dataset Address
face_sort(address) 
