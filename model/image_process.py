from PIL import Image, ImageDraw, ImageFont
import cloudinary
import cloudinary.uploader
import cloudinary.api
import requests

cloudinary.config(
    cloud_name="dheikvmxu",
    api_key="315526953864782",
    api_secret="EFpDy_CPsVNzVWor9gmY1oZ_XPc"
)


class ImageProcess:
    BASE_IMAGE_PATH = "base/certification_base.png"
    draw_info = {}
    year: str
    student_number: str
    student_name: str
    date: str
    department_name: str
    president_name: str
    study_name: str

    def __init__(self, department_name: str, student_number: str, student_name: str, year: str, president_name: str, date: str, study_name: str):
        self.date = date
        self.year = year
        self.student_number = student_number
        self.student_name = student_name
        self.department_name = department_name
        self.president_name = president_name
        self.study_name = study_name

        self.draw_info = {
            "department_name_student_number": {
                "text": department_name+" "+student_number,
                "position": (333, 322),
                "text_color": (139, 139, 139),
                "font": ImageFont.truetype("font/GmarketSansTTFLight.ttf", 13),
            },
            "student_name": {
                "text": student_name,
                "position": (369, 350),
                "text_color": (0, 0, 0),
                "font": ImageFont.truetype("font/GmarketSansTTFMedium.ttf", 36),
            },
            "year": {
                "text": "포리프 "+year+"년도 회장",
                "position": (564, 473),
                "text_color": (0, 0, 0),
                "font": ImageFont.truetype("font/GmarketSansTTFMedium.ttf", 12),
            },
            "president_name": {
                "text": president_name,
                "position": (564, 491),
                "text_color": (0, 0, 0),
                "font": ImageFont.truetype("font/GmarketSansTTFLight.ttf", 14),
            },

            "date": {
                "text": date,
                "position": (140, 474),
                "text_color": (18, 18, 18),
                "font": ImageFont.truetype("font/GmarketSansTTFLight.ttf", 13),
            },
            "study_name": {
                "text": study_name,
                "position": (94, 495),
                "text_color": (18, 18, 18),
                "font": ImageFont.truetype("font/GmarketSansTTFLight.ttf", 13),
            },
        }

    def _generate_certification(self):
        output_path = "output/"+self.year+"/"+self.student_number+".png"
        image = Image.open(self.BASE_IMAGE_PATH)
        draw = ImageDraw.Draw(image)

        for i in self.draw_info:
            draw.text(self.draw_info[i]["position"], self.draw_info[i]["text"],
                      font=self.draw_info[i]["font"], fill=self.draw_info[i]["text_color"], align="center")
        image.save(output_path)
        return output_path

    def _image_upload(self, path: str) -> str:
        result = cloudinary.uploader.upload(
            path, folder='NFTs')
        return result["secure_url"]

    def _generate_json(self, uri: str):
        json_server: str = "https://baseURL/v1/cert-jsons"
        datas = {
            "image": uri,
            "name": self.study_name+" "+self.student_number,
            "study": self.study_name,
        }
        response = requests.post(json_server, data=datas)
        if (response.status_code != 200):
            print(response.status_code)
            print(response.json())
            return None
        return json_server+'/'+str(response.json()["uri"])

    def run(self):
        path = self._generate_certification()
        uri = self._image_upload(path)
        return uri
        # return self._generate_json(uri)
