
###############################################################################
#
# PutBucketACL
# Sets the access control list (ACL) permissions for an existing bucket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PutBucketACL(Choreography):

    """
    Create a new instance of the PutBucketACL Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/PutBucketACL')


    def new_input_set(self):
        return PutBucketACLInputSet()

    def _make_result_set(self, result, path):
        return PutBucketACLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketACLChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PutBucketACL
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PutBucketACLInputSet(InputSet):
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
        Set the value of the BucketName input for this choreography. ((required, string) The name of the bucket to create or update a policy for.)
        """
        def set_BucketName(self, value):
            InputSet._set_input(self, 'BucketName', value)

        """
        Set the value of the GranteeEmailAddress input for this choreography. ((required, string) The email address of the grantee.)
        """
        def set_GranteeEmailAddress(self, value):
            InputSet._set_input(self, 'GranteeEmailAddress', value)

        """
        Set the value of the GranteeId input for this choreography. ((required, string) The canonical user id of the grantee.)
        """
        def set_GranteeId(self, value):
            InputSet._set_input(self, 'GranteeId', value)

        """
        Set the value of the OwnerEmailAddress input for this choreography. ((required, string) The email address of the owner who is granting permission.)
        """
        def set_OwnerEmailAddress(self, value):
            InputSet._set_input(self, 'OwnerEmailAddress', value)

        """
        Set the value of the OwnerId input for this choreography. ((required, string) The canonical user id of the owner who is granting permission.)
        """
        def set_OwnerId(self, value):
            InputSet._set_input(self, 'OwnerId', value)

        """
        Set the value of the Permission input for this choreography. ((required, string) The permission you are granting (i.e. FULL_CONTROL).)
        """
        def set_Permission(self, value):
            InputSet._set_input(self, 'Permission', value)


"""
A ResultSet with methods tailored to the values returned by the PutBucketACL choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PutBucketACLResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon. Note that for a successful ACL creation, no content is returned and this output variable should be empty.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PutBucketACLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PutBucketACLResultSet(response, path)
