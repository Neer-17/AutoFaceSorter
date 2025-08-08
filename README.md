# AutoFaceSorter
A Python tool that automatically sorts images into folders based on detected faces using face recognition. Ideal for organizing photo collections by person.

## 🚀 Features

- Detects faces in all images of a folder
- Groups images by the same person's face
- Creates separate folders for each unique face
- Skips images with no faces or multiple faces (optional)
- CLI support for batch sorting

## 🖼️ How it Works

1. Uses `face_recognition` to extract facial embeddings
2. Compares each face with existing ones
3. If a match is found, image goes into that person's folder
4. Otherwise, a new folder is created for a new face

## 📁 Folder Structure (Output Example)
dataset/
├── Person_1/
│ ├── img1.jpg
│ └── img3.jpg
├── Person_2/
│ └── img2.jpg
└── Others/
└── img4.jpg

📌 To-Do
 GUI using Tkinter or PyQt

 Add cloud support (e.g., Google Drive or Dropbox)

 Support for multiple faces per image

🙋‍♂️ Author
Made with ❤️ by Neeraj Panwar
GitHub: @neerajpanwar
