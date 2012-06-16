
###############################################################################
#
# CreateImage
# Creates an Amazon Machine Image from an Amazon EBS-backed instance. The image can be used later to launch other identical servers.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateImage(Choreography):

    """
    Create a new instance of the CreateImage Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/CreateImage')


    def new_input_set(self):
        return CreateImageInputSet()

    def _make_result_set(self, result, path):
        return CreateImageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateImageChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateImage
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateImageInputSet(InputSet):
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
        Set the value of the Description input for this choreography. ((optional, string) A description for the image you want to create.)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the InstanceId input for this choreography. ((required, string) The ID of the instance to create the image on.)
        """
        def set_InstanceId(self, value):
            InputSet._set_input(self, 'InstanceId', value)

        """
        Set the value of the Name input for this choreography. ((required, string) The name for the image you are creating.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the NoReboot input for this choreography. ((optional, boolean) Defaults to false. Amazon EC2 will attempt to shut down the instance before and after creating the image. Set to 1 for NoReboot.)
        """
        def set_NoReboot(self, value):
            InputSet._set_input(self, 'NoReboot', value)


"""
A ResultSet with methods tailored to the values returned by the CreateImage choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateImageResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateImageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateImageResultSet(response, path)
