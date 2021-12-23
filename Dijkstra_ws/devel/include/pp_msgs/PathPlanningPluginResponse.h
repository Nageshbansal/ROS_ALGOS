// Generated by gencpp from file pp_msgs/PathPlanningPluginResponse.msg
// DO NOT EDIT!


#ifndef PP_MSGS_MESSAGE_PATHPLANNINGPLUGINRESPONSE_H
#define PP_MSGS_MESSAGE_PATHPLANNINGPLUGINRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pp_msgs
{
template <class ContainerAllocator>
struct PathPlanningPluginResponse_
{
  typedef PathPlanningPluginResponse_<ContainerAllocator> Type;

  PathPlanningPluginResponse_()
    : plan()  {
    }
  PathPlanningPluginResponse_(const ContainerAllocator& _alloc)
    : plan(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _plan_type;
  _plan_type plan;





  typedef boost::shared_ptr< ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator> const> ConstPtr;

}; // struct PathPlanningPluginResponse_

typedef ::pp_msgs::PathPlanningPluginResponse_<std::allocator<void> > PathPlanningPluginResponse;

typedef boost::shared_ptr< ::pp_msgs::PathPlanningPluginResponse > PathPlanningPluginResponsePtr;
typedef boost::shared_ptr< ::pp_msgs::PathPlanningPluginResponse const> PathPlanningPluginResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator1> & lhs, const ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator2> & rhs)
{
  return lhs.plan == rhs.plan;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator1> & lhs, const ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace pp_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d00db495743883c1d9a4cf3d0844ceac";
  }

  static const char* value(const ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd00db495743883c1ULL;
  static const uint64_t static_value2 = 0xd9a4cf3d0844ceacULL;
};

template<class ContainerAllocator>
struct DataType< ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pp_msgs/PathPlanningPluginResponse";
  }

  static const char* value(const ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32[] plan\n"
;
  }

  static const char* value(const ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.plan);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PathPlanningPluginResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pp_msgs::PathPlanningPluginResponse_<ContainerAllocator>& v)
  {
    s << indent << "plan[]" << std::endl;
    for (size_t i = 0; i < v.plan.size(); ++i)
    {
      s << indent << "  plan[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.plan[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // PP_MSGS_MESSAGE_PATHPLANNINGPLUGINRESPONSE_H
