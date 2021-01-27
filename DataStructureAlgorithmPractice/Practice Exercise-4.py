class Course:
    def __init__(self,title,instructor,price,lectures):
        self.title=title
        self.instructor=instructor
        self.price=price
        self.lectures=lectures
        self.users=[]
        self.rating=0
        self.avg_rating=0
    
    def __str__(self):
         return f'{self.title} by {self.instructor}'

    def new_user_enrolled(self,user):
        self.users.append(user)
        print("New user Enrolled",user)

    def received_a_rating(self,rating):
        self.avg_rating=(self.avg_rating*self.rating+rating)/(self.rating+1)
        self.rating+=1

    def show_details(self):
        print("Course Title:", self.title)
        print("Instructor:", self.instructor)
        print("Price:", self.price)
        print("No of Lectures:", self.lectures)
        print("Users:",self.users)
        print('Average rating : ', self.avg_rating)
        print("No of ratings:",self.rating)

    
class VideoCourse(Course):
    def __init__(self,title,instructor,price,lectures,length_video):
        super().__init__(title,instructor,price,lectures)
        self.length_video=length_video
    def show_details(self):
        super().show_details()
        print("Length of Video:",self.length_video)

class PdfCourse(Course):
    def __init__(self,title,instructor,price,lectures,pages):
        super().__init__(title,instructor,price,lectures)
        self.pages=pages
    def show_details(self):
        super().show_details()
        print("No of pages:",self.pages)

vc=VideoCourse("Python","ABC",2400,20,5)
vc.new_user_enrolled('Allen')
vc.new_user_enrolled('Max')
vc.new_user_enrolled('Tom')
vc.received_a_rating(3)
vc.received_a_rating(5)
vc.received_a_rating(4)
vc.show_details()
pc=PdfCourse("Java","DEF",500,20,200)
pc.new_user_enrolled('Allen')
pc.new_user_enrolled('Mary')
pc.new_user_enrolled('JIm')
pc.received_a_rating(5)
pc.received_a_rating(4)
pc.received_a_rating(4.5)
pc.show_details()