class DockerContainer:
    def __init__(self,name,image):
        self.name=name
        self.iimage=image
        self.running=false
    
    def start(self):
        self.running=true
        print(self.name, "started")
    def status(self):
        print("running": self.running)
    
c1 = DockerContainer("nginx", nginx:latest)

c1.start();
c1.status();