import cv2
import imutils
import datetime
from src.apis.sound import Sound
from src.views.views import Views
from imutils.video import VideoStream
from src.apis.randomName import Generator
from src.models.captures.image_capture import Image
from src.apis.detectNPredict import detect_and_predict_mask

from src.logging.logging import log


class Stream(Views, Image) :

    def __init__(self) :

        super().__init__()

    def video_stream(self, face_net, mask_net) :

        # initialize the video stream
        print(f"[ INFO ] starting video stream...")
        vs = VideoStream(0).start()

        """
            Visitors index

        """
        MASK_VISITORS   = 0
        NOMASK_VISITORS = 0

        TOTAL_VISITORS  = 0

        # loop over the frames from the video stream
        while True:

            # grab the frame from the threaded video stream and resize it
            # to have a maximum width of 400 pixels
            frame = vs.read()
            frame = imutils.resize( frame, width=1024 )

            # detect faces in the frame and determine if they are wearing a
            # face mask or not
            (locs, preds) = detect_and_predict_mask(frame, face_net, mask_net)

            # loop over the detected face locations and their corresponding
            # locations

            PERCENTAGES = {

                "response" : False

            }

            for (box, pred) in zip(locs, preds):

                # unpack the bounding box and predictions
                (startX, startY, endX, endY) = box
                (mask, withoutMask) = pred

                # determine the class label and color we'll use to draw
                # the bounding box and text
                if mask > withoutMask :

                    PERCENTAGES = {

                        "response" : True,
                        "capture" : f'documentations/capture/mask/{Generator().generate()}.jpg',
                        "label"   : "silahkan.... Anda boleh masuk",
                        "status"   : "MASK",
                        "sound"   : "src/asset/sound/mask.mp3",
                        "color"   : (0, 255, 0),
                        "percentages" : f"{int(max(mask, withoutMask) * 100)} %",
                        "ends"   : (endX, endY),
                        "starts" : (startX, startY - 10)

                    }

                    MASK_VISITORS  += 1
                    TOTAL_VISITORS += 1

                    


                elif mask < withoutMask :

                    PERCENTAGES = {

                        "response" : True,
                        "capture" : f'documentations/capture/no_mask/{Generator().generate()}.jpg',
                        "label"   : "PAKAI MASKER DAHULU!!!",
                        "status"   : "NOMASK",
                        "sound"   : "src/asset/sound/nomask.mp3",
                        "color"   : (0, 0, 255),
                        "percentages" : f"{int(max(mask, withoutMask) * 100)} %",
                        "ends"   : (endX, endY),
                        "starts" : (startX, startY - 10)

                    }

                    NOMASK_VISITORS += 1
                    TOTAL_VISITORS  += 1

                    


            if PERCENTAGES["response"] :

                """ image capture """
                self.capture(

                    frame    = frame,
                    location = PERCENTAGES["capture"]

                )

                """ face detect view """
                self.face_detectView(

                    frame  = frame,
                    label  = PERCENTAGES["label"], 
                    starts = PERCENTAGES["starts"], 
                    ends   = PERCENTAGES["ends"], 
                    color  = PERCENTAGES["color"]

                )

                """ percentage view """
                self.percentagesView(

                    frame      = frame, 
                    status     = PERCENTAGES["status"],
                    percentage = PERCENTAGES["percentages"],
                    color      = PERCENTAGES["color"]

                )

                """ sound """
                Sound( source = PERCENTAGES["sound"] )

                """ logging """
                log( message = PERCENTAGES["status"] )

            else :

                self.noHumanView( frame = frame )



            # visitors
            self.visitorsView(

                frame           = frame,
                mask_visitors   = MASK_VISITORS,
                nomask_visitors = NOMASK_VISITORS,
                total_visitors  = TOTAL_VISITORS

            )
            # cv2.putText(frame, f"MASK    : {MASK_VISITORS} orang", (20, 595),cv2.FONT_HERSHEY_SIMPLEX, 0.70, (255, 255, 255), 2)
            # cv2.putText(frame, f"NOMASK : {NOMASK_VISITORS} orang", (20, 625),cv2.FONT_HERSHEY_SIMPLEX, 0.70, (255, 255, 255), 2)
            # cv2.putText(frame, "------------- +", (20, 645),cv2.FONT_HERSHEY_SIMPLEX, 0.70, (255, 255, 255), 2)
            # cv2.putText(frame, f"TOTAL   : {TOTAL_VISITORS} orang", (20, 670),cv2.FONT_HERSHEY_SIMPLEX, 0.70, (255, 255, 255), 2) 	

            # timer
            self.timerView( frame = frame )
            # cv2.putText(frame, f"{datetime.datetime.now().strftime('%H:%M:%S')}", (860, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.90, (255, 255, 255), 2)		

            # connction
            self.connectionView( frame = frame )
            # cv2.putText(frame, f"OFFLINE", (860, 670),cv2.FONT_HERSHEY_SIMPLEX, 0.90, (0, 0, 255), 2)

            # show the output frame
            cv2.imshow("ZEIPER", frame)
            key = cv2.waitKey(1) & 0xFF
            
            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break

        # do a bit of cleanup
        cv2.destroyAllWindows()
        vs.stop()































