import os

def change_class_yolo_annotation(annotation_file, class_mapping):
    with open(annotation_file, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        line = line.strip().split()
        if line and line[0] in class_mapping:
            line[0] = class_mapping[line[0]]
            new_lines.append(' '.join(line))

    with open(annotation_file, 'w') as file:
        file.write('\n'.join(new_lines))



def change_class_in_folder(folder_path, class_mapping):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            annotation_file = os.path.join(folder_path, file_name)
            change_class_yolo_annotation(annotation_file, class_mapping)


# Example usage
folder_path = '/path/to/your/folder'

#keys in dict are class values in original dataset annotation
#value in key value pair is the desired annotation value
class_mapping = {'0': '1',  '2': '0', '3': '1'}
change_class_in_folder(folder_path, class_mapping)
