import service.image_process_v2 as image_process
import service.NFT_process as NFT_process
import service.process_facade as process_facade


if __name__ == "__main__":
    print(len("웹스크래핑 스터디(정규)"))
    image_process_instance = image_process.ImageProcessV2(
        date="2024.02.15", department_name="정보시스템학과", student_name="김아무", student_number="2023001002", study_name="웹스크래핑 스터디(정규)", durations="2023.07.01~2023.12.31")
    image_process_instance.run()
