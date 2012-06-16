
###############################################################################
#
# DeregisterImage
# Deregisters the specified AMI.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeregisterImage(Choreography):

    """
    Create a new instance of the DeregisterImage Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/DeregisterImage')


    def new_input_set(self):
        return DeregisterImageInputSet()

    def _make_result_set(self, result, path):
        return DeregisterImageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeregisterImageChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeregisterImage
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeregisterImageInputSet(InputSet):
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
        Set the value of the ImageId input for this choreography. ((required, string) The AMI ID.)
        """
        def set_ImageId(self, value):
            InputSet._set_input(self, 'ImageId', value)


"""
A ResultSet with methods tailored to the values returned by the DeregisterImage choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeregisterImageResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeregisterImageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeregisterImageResultSet(response, path)
