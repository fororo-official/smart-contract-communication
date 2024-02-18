from PIL import Image, ImageDraw, ImageFont


class ImageProcessV2:
    BASE_IMAGE_PATH = "base/certification_base_v2.png"
    date: str
    department_name: str
    student_number: str
    student_name: str
    study_name: str
    durations: str
    draw_info: dict

    def __init__(self, date: str, department_name: str, student_number: str, student_name: str, study_name: str, durations: str):
        self.date = date
        self.department_name = department_name
        self.student_number = student_number
        self.student_name = student_name
        self.study_name = study_name
        self.durations = durations
        self.draw_info = {
            "date": {
                "text": date,
                "position": (348, 206),
                "text_color": (0, 0, 0),
                "font": ImageFont.truetype("font/GmarketSansTTFMedium.ttf", 21),
            },

            "department_name": {
                "text": department_name,
                "position": (594, 206),
                "text_color": (0, 0, 0),
                "font": ImageFont.truetype("font/GmarketSansTTFMedium.ttf", 21),
            },

            "student_number": {
                "text": student_number,
                "position": (870, 206),
                "text_color": (0, 0, 0),
                "font": ImageFont.truetype("font/GmarketSansTTFMedium.ttf", 21),
            },
            "student_name": {
                "text": student_name,
                "position": ((1280-ImageFont.truetype("font/GmarketSansTTFMedium.ttf", 48).getlength(student_name))//2, 297),
                "text_color": (0, 0, 0),
                "font": ImageFont.truetype("font/GmarketSansTTFMedium.ttf", 48),
            },
            "study_name": {
                "text": study_name,
                "position": ((1280 - ImageFont.truetype("font/GmarketSansTTFMedium.ttf", 48).getlength(study_name))//2, 430),
                "text_color": (0, 0, 0),
                "font": ImageFont.truetype("font/GmarketSansTTFMedium.ttf", 48),
            },

            "durations": {
                "text": durations,
                "position": (530, 536),
                "text_color": (139, 139, 139),
                "font": ImageFont.truetype("font/GmarketSansTTFLight.ttf", 19),
            },

        }

    def _generate_certification(self):
        print(self)
        output_path = "output/"+self.student_number+"-"+self.date+".png"
        image = Image.open(self.BASE_IMAGE_PATH)
        draw = ImageDraw.Draw(image)

        for i in self.draw_info:
            draw.text(self.draw_info[i]["position"], self.draw_info[i]["text"],
                      font=self.draw_info[i]["font"], fill=self.draw_info[i]["text_color"], align='center')
        image.save(output_path)
        return output_path

    def _image_upload(self, path: str) -> str:
        print(path + "에 있는 파일을 업로드 합니다...")
        print("기능 구현 필요")

        return "uri"

    def run(self) -> str:
        path = self._generate_certification()
        uri = self._image_upload(path)
        return uri
