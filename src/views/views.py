import cv2
import datetime

class Views :

    def face_detectView(self, frame, label, starts, ends, color) :

        cv2.rectangle(frame, starts, ends, color, 2)
        cv2.putText(frame, label, starts, cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        
    def percentagesView(self, frame, status, percentage, color) :

        cv2.putText(frame, status, (170, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.70, color, 2)
        cv2.putText(frame, "status      :", (20, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.70, (255, 255, 255), 2)

        cv2.putText(frame, percentage, (170, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.70, color, 2)
        cv2.putText(frame, "persentase :", (20, 75),cv2.FONT_HERSHEY_SIMPLEX, 0.70, (255, 255, 255), 2)

    def visitorsView(self, frame, mask_visitors, nomask_visitors, total_visitors) :

        cv2.putText(frame, f"MASK    : {mask_visitors} orang", (20, 595),cv2.FONT_HERSHEY_SIMPLEX, 0.70, (255, 255, 255), 2)
        cv2.putText(frame, f"NOMASK : {nomask_visitors} orang", (20, 625),cv2.FONT_HERSHEY_SIMPLEX, 0.70, (255, 255, 255), 2)
        cv2.putText(frame, "------------- +", (20, 645),cv2.FONT_HERSHEY_SIMPLEX, 0.70, (255, 255, 255), 2)
        cv2.putText(frame, f"TOTAL   : {total_visitors} orang", (20, 670),cv2.FONT_HERSHEY_SIMPLEX, 0.70, (255, 255, 255), 2) 

    def timerView(self, frame) :

        cv2.putText(frame, f"{datetime.datetime.now().strftime('%H:%M:%S')}", (860, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.90, (255, 255, 255), 2)

    def connectionView(self, frame) :

        cv2.putText(frame, f"OFFLINE", (860, 670),cv2.FONT_HERSHEY_SIMPLEX, 0.90, (0, 0, 255), 2)

    def noHumanView(self, frame) :

        cv2.putText(frame, "NO HUMAN", (20, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.90, (255, 255, 255), 2)






































































