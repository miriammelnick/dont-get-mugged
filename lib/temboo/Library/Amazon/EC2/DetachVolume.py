
###############################################################################
#
# DetachVolume
# Detaches an Amazon EBS volume from an instance.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DetachVolume(Choreography):

    """
    Create a new instance of the DetachVolume Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/DetachVolume')


    def new_input_set(self):
        return DetachVolumeInputSet()

    def _make_result_set(self, result, path):
        return DetachVolumeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DetachVolumeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DetachVolume
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DetachVolumeInputSet(InputSet):
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
        Set the value of the Device input for this choreography. ((optional, string) The device name.)
        """
        def set_Device(self, value):
            InputSet._set_input(self, 'Device', value)

        """
        Set the value of the InstanceId input for this choreography. ((optional, string) The ID of the instance.)
        """
        def set_InstanceId(self, value):
            InputSet._set_input(self, 'InstanceId', value)

        """
        Set the value of the VolumeId input for this choreography. ((required, string) The ID of the volume.)
        """
        def set_VolumeId(self, value):
            InputSet._set_input(self, 'VolumeId', value)


"""
A ResultSet with methods tailored to the values returned by the DetachVolume choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DetachVolumeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DetachVolumeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DetachVolumeResultSet(response, path)
