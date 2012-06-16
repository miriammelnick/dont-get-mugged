
###############################################################################
#
# CreateSnapshot
# Create a snapshot from a specified EBS volume.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateSnapshot(Choreography):

    """
    Create a new instance of the CreateSnapshot Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/CreateSnapshot')


    def new_input_set(self):
        return CreateSnapshotInputSet()

    def _make_result_set(self, result, path):
        return CreateSnapshotResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateSnapshotChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateSnapshot
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateSnapshotInputSet(InputSet):
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
        Set the value of the Description input for this choreography. ((optional, string) A description for the volume that you want to create.)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the VolumeId input for this choreography. ((required, string) The id of the EBS volume to snapshot.)
        """
        def set_VolumeId(self, value):
            InputSet._set_input(self, 'VolumeId', value)


"""
A ResultSet with methods tailored to the values returned by the CreateSnapshot choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateSnapshotResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateSnapshotChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateSnapshotResultSet(response, path)
