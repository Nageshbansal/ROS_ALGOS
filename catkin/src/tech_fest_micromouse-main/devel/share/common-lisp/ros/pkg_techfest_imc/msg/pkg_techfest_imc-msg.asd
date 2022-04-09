
(cl:in-package :asdf)

(defsystem "pkg_techfest_imc-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "dest" :depends-on ("_package_dest"))
    (:file "_package_dest" :depends-on ("_package"))
  ))