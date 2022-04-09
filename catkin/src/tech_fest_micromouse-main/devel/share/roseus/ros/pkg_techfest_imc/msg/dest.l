;; Auto-generated. Do not edit!


(when (boundp 'pkg_techfest_imc::dest)
  (if (not (find-package "PKG_TECHFEST_IMC"))
    (make-package "PKG_TECHFEST_IMC"))
  (shadow 'dest (find-package "PKG_TECHFEST_IMC")))
(unless (find-package "PKG_TECHFEST_IMC::DEST")
  (make-package "PKG_TECHFEST_IMC::DEST"))

(in-package "ROS")
;;//! \htmlinclude dest.msg.html


(defclass pkg_techfest_imc::dest
  :super ros::object
  :slots (_dest_x_coordinate _dest_y_coordinate ))

(defmethod pkg_techfest_imc::dest
  (:init
   (&key
    ((:dest_x_coordinate __dest_x_coordinate) 0.0)
    ((:dest_y_coordinate __dest_y_coordinate) 0.0)
    )
   (send-super :init)
   (setq _dest_x_coordinate (float __dest_x_coordinate))
   (setq _dest_y_coordinate (float __dest_y_coordinate))
   self)
  (:dest_x_coordinate
   (&optional __dest_x_coordinate)
   (if __dest_x_coordinate (setq _dest_x_coordinate __dest_x_coordinate)) _dest_x_coordinate)
  (:dest_y_coordinate
   (&optional __dest_y_coordinate)
   (if __dest_y_coordinate (setq _dest_y_coordinate __dest_y_coordinate)) _dest_y_coordinate)
  (:serialization-length
   ()
   (+
    ;; float64 _dest_x_coordinate
    8
    ;; float64 _dest_y_coordinate
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _dest_x_coordinate
       (sys::poke _dest_x_coordinate (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _dest_y_coordinate
       (sys::poke _dest_y_coordinate (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _dest_x_coordinate
     (setq _dest_x_coordinate (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _dest_y_coordinate
     (setq _dest_y_coordinate (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get pkg_techfest_imc::dest :md5sum-) "cf363d99a20f66b06e0d4259cb1930ec")
(setf (get pkg_techfest_imc::dest :datatype-) "pkg_techfest_imc/dest")
(setf (get pkg_techfest_imc::dest :definition-)
      "float64 dest_x_coordinate
float64 dest_y_coordinate

")



(provide :pkg_techfest_imc/dest "cf363d99a20f66b06e0d4259cb1930ec")


