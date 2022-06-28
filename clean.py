import shutil
import os


def cleanUp(user, pdf, image, screenshot):
    desktop_dir = 'C:/Users/{0}/Desktop'.format(user)
    screenshot_dir = 'C:/Users/{0}/Desktop/ScreenShots'.format(user)
    image_dir = 'C:/Users/{0}/Desktop/Images'.format(user)
    pdf_dir = 'C:/Users/{0}/Desktop/PDFs'.format(user)
    # This will move Screen Shots:

    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
        print('Creating screenshot folder ')

    files_on_desktop = os.listdir(desktop_dir)

    for file in files_on_desktop:
        if file.endswith('.png') or file.endswith('.PNG'):
            file_dir = desktop_dir + '/' + file
            shutil.move(file_dir, screenshot_dir)
            print(f'Moving {file}...')

    # This will move images:
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
        print('Creating image folder ')

    for file in files_on_desktop:
        if file.endswith('.jpg') or file.endswith('.JPG'):
            file_dir = desktop_dir + '/' + file
            shutil.move(file_dir, image_dir)
            print(f'Moving {file}...')

    # This will move pdfs:
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)
        print('Creating pdf folder ')

    for file in files_on_desktop:
        if file.endswith('.pdf') or file.endswith('.PDF'):
            file_dir = desktop_dir + '/' + file
            shutil.move(file_dir, pdf_dir)
            print(f'Moving {file}...')
