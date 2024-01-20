import cv2
import mediapipe as mp
import pygame

class Cam(pygame.sprite.Sprite):
    def __init__(self):
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        #adding all the images to sprite array
        self.images = []
        self.zoneinterdite=True
        self.PourcentageLargeurCamera=35
        self.PourcentageHauteurCamera=55
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.8, min_tracking_confidence=0.9)
        self.Largeur=640
        self.Hauteur=480
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.webcam_compatibility = False
        else:
            self.webcam_compatibility = True
        self.cap.set(3, self.Largeur)
        self.cap.set(4, self.Hauteur)
        self.LargeurChampCamera = round((self.PourcentageLargeurCamera * self.Largeur)/100)
        print(self.LargeurChampCamera)
        
        self.HauteurChampCamera = round((self.PourcentageHauteurCamera * self.Hauteur)/100)
        print(self.HauteurChampCamera)
        self.LimiteGaucheCamera = round((self.Largeur-self.LargeurChampCamera)/2)
        self.LimiteDroiteCamera = round(self.Largeur-(self.Largeur-self.LargeurChampCamera)/2)
        self.LimiteBasseCamera = round((self.Hauteur-self.HauteurChampCamera)/2)
        self.LimiteHauteCamera = round(self.Hauteur-(self.Hauteur-self.HauteurChampCamera)/2)
        ret, image = self.cap.read()


    def update(self, cap, mp_drawing, mp_pose, LimiteBasseCamera, LimiteHauteCamera, LimiteGaucheCamera, LimiteDroiteCamera ):
        
        self.photo = cap.read()[1]
        self.photo = cv2.flip(self.photo,1)
        self.photo = self.photo[self.LimiteBasseCamera:self.LimiteHauteCamera,self.LimiteGaucheCamera:self.LimiteDroiteCamera]
        self.RGB = cv2.cvtColor(self.photo, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(self.RGB)
        
        if self.results.pose_landmarks:
            for i in range(1, 32):
                self.posY = self.results.pose_landmarks.landmark[i].y*self.HauteurChampCamera
                if self.posY > 0 and self.posY < self.HauteurChampCamera :
                    self.zoneinterdite = False
                else:
                    self.zoneinterdite = True
                    mp_drawing.draw_landmarks(self.photo, self.results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        else:
            self.zoneinterdite = True
        
        if self.zoneinterdite == False:
            mp_drawing.draw_landmarks(self.photo, self.results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        self.photo = cv2.cvtColor(self.photo, cv2.COLOR_BGR2RGB)
        self.cam = pygame.surfarray.make_surface(self.photo)
        self.cam = pygame.transform.scale(self.cam, (  1.45 * self.cam.get_width(),  self.cam.get_height()))
        self.cam = pygame.transform.rotate(self.cam, -90)
        self.images = self.cam
        self.rect = self.images.get_rect()
        
