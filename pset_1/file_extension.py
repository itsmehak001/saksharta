filename = input("Enter the filename: ")

extension = filename.split(".")[-1]

if extension in ["jpg", "jpeg", "png", "gif"]:
    print("Image file (Correct)")
elif extension in ["txt", "doc", "docx", "pdf"]:
    print("Document file")
elif extension in ["mp3", "wav", "ogg"]:
    print("Audio file")
elif extension in ["mp4", "avi", "mkv"]:
    print("Video file")
else:
    print("file_extension.py ")