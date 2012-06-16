
###############################################################################
#
# ModifyImageAttribute
# Modifies an attribute of an AMI.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ModifyImageAttribute(Choreography):

    """
    Create a new instance of the ModifyImageAttribute Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/ModifyImageAttribute')


    def new_input_set(self):
        return ModifyImageAttributeInputSet()

    def _make_result_set(self, result, path):
        return ModifyImageAttributeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ModifyImageAttributeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ModifyImageAttribute
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ModifyImageAttributeInputSet(InputSet):
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
        Set the value of the AddGroup input for this choreography. ((optional, string) Adds the specified group to the image's list of launch permissions. The only valid value is "all".)
        """
        def set_AddGroup(self, value):
            InputSet._set_input(self, 'AddGroup', value)

        """
        Set the value of the AddUserId input for this choreography. ((optional, string) Adds the specified AWS account ID to the AMI's list of launch permissions.)
        """
        def set_AddUserId(self, value):
            InputSet._set_input(self, 'AddUserId', value)

        """
        Set the value of the Description input for this choreography. ((optional, string) Changes the AMI's description to the specified value.)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the ImageId input for this choreography. ((required, string) The AMI ID.)
        """
        def set_ImageId(self, value):
            InputSet._set_input(self, 'ImageId', value)

        """
        Set the value of the ProductCode input for this choreography. ((optional, string) Adds the specified product code to the specified Amazon S3-backed AMI. Once you add a product code to an AMI, it can't be removed.)
        """
        def set_ProductCode(self, value):
            InputSet._set_input(self, 'ProductCode', value)

        """
        Set the value of the RemoveGroup input for this choreography. ((optional, string) Removes the specified group from the image's list of launch permissions. The only valid value is "all".)
        """
        def set_RemoveGroup(self, value):
            InputSet._set_input(self, 'RemoveGroup', value)

        """
        Set the value of the RemoveUserId input for this choreography. ((optional, string) Removes the specified AWS account ID from the AMI's list of launch permissions.)
        """
        def set_RemoveUserId(self, value):
            InputSet._set_input(self, 'RemoveUserId', value)


"""
A ResultSet with methods tailored to the values returned by the ModifyImageAttribute choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ModifyImageAttributeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ModifyImageAttributeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ModifyImageAttributeResultSet(response, path)
