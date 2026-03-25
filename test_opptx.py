from OptigoUtils.opptx.PPTX_Generator import PPTX_Generator

image_paths = [r'C:\Users\Public\Pictures\Sample Pictures\Hydrangeas.jpg',
               r'C:\Users\Public\Pictures\Sample Pictures\Chrysanthemum.jpg',
               r'C:\Users\Public\Pictures\Sample Pictures\Desert.jpg',
               r'C:\Users\Public\Pictures\Sample Pictures\Penguins.jpg']

configuration_filename = "OptigoUtils/opptx/Slide_1_Template.json"

h_pptx = PPTX_Generator()
h_slide = h_pptx.create_slide_template(configuration_filename)

h_slide.set_line(0, 'Main Title', 'd:\\TEMP')
h_slide.set_line(1, 'Second line...')
h_slide.set_line(2, 'Last Line !!!')

actions = [ '"C:/OptigO/Clip Analyzer/Clip Analyzer Shell.exe" "W:/Trophy_DB/Implants/210114/IL213/1/RAW_Data/CH2/CamelA1_CamelB2_df112.xvi" 200 298 134',
            '"C:/OptigO/Clip Analyzer/Clip Analyzer Shell.exe" "W:/Trophy_DB/Implants/210114/IL213/1/RAW_Data/CH3/CamelA1_CamelB2_df112.xvi" 200 298 134',
            '"C:/OptigO/Clip Analyzer/Clip Analyzer Shell.exe" "W:/Trophy_DB/Implants/210114/IL213/1/RAW_Data/CH0/CamelA1_CamelB2_df112.xvi" 200 999 999',
            '"C:/OptigO/Clip Analyzer/Clip Analyzer Shell.exe" "W:/Trophy_DB/Implants/210114/IL213/1/RAW_Data/CH1/CamelA1_CamelB2_df112.xvi" 200 999 999']
# file:///C:\\OptigO\\Clip%20Analyzer\\Clip%20Analyzer%20Shell.exe
for y in range(4):
    for x in range(3):
        h_slide.set_image(x, y, image_paths[(x + y * 3) % 4], actions[(x + y * 3) % 4])
h_pptx.add_slide(h_slide)

h_pptx.save('P1.pptx')
