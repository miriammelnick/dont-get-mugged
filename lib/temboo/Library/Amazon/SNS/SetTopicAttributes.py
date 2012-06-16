
###############################################################################
#
# SetTopicAttributes
# Allows a topic owner to update the attribute of a topic to a new value.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SetTopicAttributes(Choreography):

    """
    Create a new instance of the SetTopicAttributes Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SNS/SetTopicAttributes')


    def new_input_set(self):
        return SetTopicAttributesInputSet()

    def _make_result_set(self, result, path):
        return SetTopicAttributesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SetTopicAttributesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SetTopicAttributes
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SetTopicAttributesInputSet(InputSet):
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
        Set the value of the AttributeName input for this choreography. ((required, string) The name of the attribute you want to modify. Valid values are: Policy and DisplayName.)
        """
        def set_AttributeName(self, value):
            InputSet._set_input(self, 'AttributeName', value)

        """
        Set the value of the AttributeValue input for this choreography. ((required, string) The new value for the attribute that you want to update.)
        """
        def set_AttributeValue(self, value):
            InputSet._set_input(self, 'AttributeValue', value)

        """
        Set the value of the TopicArn input for this choreography. ((required, string) The ARN of the topic that has an attribute that you want to set.)
        """
        def set_TopicArn(self, value):
            InputSet._set_input(self, 'TopicArn', value)


"""
A ResultSet with methods tailored to the values returned by the SetTopicAttributes choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SetTopicAttributesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SetTopicAttributesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SetTopicAttributesResultSet(response, path)
