
###############################################################################
#
# CreateTopic
# Creates a new topic that notifications can be published to.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateTopic(Choreography):

    """
    Create a new instance of the CreateTopic Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SNS/CreateTopic')


    def new_input_set(self):
        return CreateTopicInputSet()

    def _make_result_set(self, result, path):
        return CreateTopicResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateTopicChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateTopic
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateTopicInputSet(InputSet):
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
        Set the value of the Name input for this choreography. ((required, string) The name of the topic you want to create.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)


"""
A ResultSet with methods tailored to the values returned by the CreateTopic choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateTopicResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateTopicChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateTopicResultSet(response, path)
