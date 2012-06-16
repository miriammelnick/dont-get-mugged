
###############################################################################
#
# RevokeDBSecurityGroupIngress
# Revokes access from a DBSecurityGroup for previously authorized IP ranges or EC2 Security Groups.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RevokeDBSecurityGroupIngress(Choreography):

    """
    Create a new instance of the RevokeDBSecurityGroupIngress Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/RevokeDBSecurityGroupIngress')


    def new_input_set(self):
        return RevokeDBSecurityGroupIngressInputSet()

    def _make_result_set(self, result, path):
        return RevokeDBSecurityGroupIngressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RevokeDBSecurityGroupIngressChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RevokeDBSecurityGroupIngress
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RevokeDBSecurityGroupIngressInputSet(InputSet):
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
        Set the value of the CIDRIP input for this choreography. ((conditional, string) IP range that should be revoked. Required unless EC2SecurityGroupName and EC2SecurityGroupOwnerId are used.)
        """
        def set_CIDRIP(self, value):
            InputSet._set_input(self, 'CIDRIP', value)

        """
        Set the value of the DBSecurityGroupName input for this choreography. ((required, string) A unique name for the security group you want to revoke ingress from.)
        """
        def set_DBSecurityGroupName(self, value):
            InputSet._set_input(self, 'DBSecurityGroupName', value)

        """
        Set the value of the EC2SecurityGroupName input for this choreography. ((conditional, string) The EC2 security group to revoke. This and EC2SecurityGroupOwnerId are required if CIDRIP is not used.)
        """
        def set_EC2SecurityGroupName(self, value):
            InputSet._set_input(self, 'EC2SecurityGroupName', value)

        """
        Set the value of the EC2SecurityGroupOwnerId input for this choreography. ((conditional, string) The account number for the security group owner to revoke. This and EC2SecurityGroupName are required if CIDRIP is not used.)
        """
        def set_EC2SecurityGroupOwnerId(self, value):
            InputSet._set_input(self, 'EC2SecurityGroupOwnerId', value)


"""
A ResultSet with methods tailored to the values returned by the RevokeDBSecurityGroupIngress choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RevokeDBSecurityGroupIngressResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RevokeDBSecurityGroupIngressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RevokeDBSecurityGroupIngressResultSet(response, path)
