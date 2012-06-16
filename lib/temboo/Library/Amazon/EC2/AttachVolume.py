
###############################################################################
#
# AttachVolume
# Attaches an Amazon EBS volume to a running instance and exposes it as the specified device.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AttachVolume(Choreography):

    """
    Create a new instance of the AttachVolume Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/AttachVolume')


    def new_input_set(self):
        return AttachVolumeInputSet()

    def _make_result_set(self, result, path):
        return AttachVolumeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AttachVolumeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AttachVolume
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AttachVolumeInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the Device input for this choreography. ((required, string) How the device is exposed to the instance (i.e. " /dev/sdh" or "xvdh").)
        """
        def set_Device(self, value):
            InputSet._set_input(self, 'Device', value)

        """
        Set the value of the InstanceId input for this choreography. ((required, string) The ID of the instance to which the volume attaches. The volume and instance must be within the same Availability Zone and the instance must be running.)
        """
        def set_InstanceId(self, value):
            InputSet._set_input(self, 'InstanceId', value)

        """
        Set the value of the VolumeId input for this choreography. ((required, string) The ID of the Amazon EBS volume. The volume and instance must be within the same Availability Zone and the instance must be running.)
        """
        def set_VolumeId(self, value):
            InputSet._set_input(self, 'VolumeId', value)


"""
A ResultSet with methods tailored to the values returned by the AttachVolume choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AttachVolumeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AttachVolumeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AttachVolumeResultSet(response, path)
