
###############################################################################
#
# CreateVolume
# Creates a new EBS volume that your EC2 instance can attach to.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateVolume(Choreography):

    """
    Create a new instance of the CreateVolume Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/CreateVolume')


    def new_input_set(self):
        return CreateVolumeInputSet()

    def _make_result_set(self, result, path):
        return CreateVolumeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateVolumeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateVolume
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateVolumeInputSet(InputSet):
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
        Set the value of the AvailabilityZone input for this choreography. ((required, string) The Availability Zone to use when creating thew new volume (i.e us-east-1a).)
        """
        def set_AvailabilityZone(self, value):
            InputSet._set_input(self, 'AvailabilityZone', value)

        """
        Set the value of the Size input for this choreography. ((conditional, integer) The size for the volume (in gigabytes) that you are creating. Valid Values are 1-1024. Required if you're not creating a volume from a snapshot.)
        """
        def set_Size(self, value):
            InputSet._set_input(self, 'Size', value)

        """
        Set the value of the SnapshotId input for this choreography. ((conditional, string) The snapshot from which to create the new volume. Required if you are creating a volume from a snapshot.)
        """
        def set_SnapshotId(self, value):
            InputSet._set_input(self, 'SnapshotId', value)


"""
A ResultSet with methods tailored to the values returned by the CreateVolume choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateVolumeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateVolumeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateVolumeResultSet(response, path)
