import model.image_process as image_process
import model.NFT_process as NFT_process
import model.process_facade as process_facade


if __name__ == "__main__":
    # 정유경 2023086880  표준성   2023063845
    image_process_instance = image_process.ImageProcess(
        department_name="정보시스템학과", student_name="표준성", student_number="2023063845", year="2023", president_name="김유진",  date="2023-12-23", study_name="포로로")
    image_process_instance.run()
    None
