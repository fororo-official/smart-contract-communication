import service.image_process as image_process
import service.NFT_process as NFT_process


class ProcessFacade:
    image_process_instance: image_process.ImageProcess
    NFT_process_instance: NFT_process.NFTProcess = NFT_process.NFTProcess()
    address = ""

    def __init__(self, department_name, studet_name, student_number, year, president_name, contents, address):
        self.image_process_instance = image_process.ImageProcess(
            department_name=department_name, studet_name=studet_name, student_number=student_number, year=year, president_name=president_name, contents=contents,
        )
        self.address = address

    def run(self):
        uri: str = self.image_process_instance.run()
        print(uri)
        result = self.NFT_process_instance.mintCertification(self.address, uri)
        print(result)
