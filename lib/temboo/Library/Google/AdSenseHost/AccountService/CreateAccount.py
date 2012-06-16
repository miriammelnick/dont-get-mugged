
###############################################################################
#
# CreateAccount
# Creates a new AdSense account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateAccount(Choreography):

    """
    Create a new instance of the CreateAccount Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/AdSenseHost/AccountService/CreateAccount')


    def new_input_set(self):
        return CreateAccountInputSet()

    def _make_result_set(self, result, path):
        return CreateAccountResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateAccountChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateAccount
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateAccountInputSet(InputSet):
        """
        Set the value of the AddContentAds input for this choreography. ((boolean) Pass in '1' to add ContentAds syndication service, '0' to omit.)
        """
        def set_AddContentAds(self, value):
            InputSet._set_input(self, 'AddContentAds', value)

        """
        Set the value of the AddSearchAds input for this choreography. ((boolean) Pass in '1' to add SearchAds syndication service, '0' to omit.)
        """
        def set_AddSearchAds(self, value):
            InputSet._set_input(self, 'AddSearchAds', value)

        """
        Set the value of the DeveloperURL input for this choreography. ((string) The site to be associated with this publisher.)
        """
        def set_DeveloperURL(self, value):
            InputSet._set_input(self, 'DeveloperURL', value)

        """
        Set the value of the EmailPromotionsPreferences input for this choreography. ((boolean) Email promotions preferences for the new account. Pass in '1' to enable and '0' to disable.)
        """
        def set_EmailPromotionsPreferences(self, value):
            InputSet._set_input(self, 'EmailPromotionsPreferences', value)

        """
        Set the value of the Email input for this choreography. ((string) The developer's email address.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) One of either 'sandbox.google.com' (for testing) or 'www.google.com'. Defaults to 'sandbox.google.com'.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the EntityType input for this choreography. ((string) One of 'Individual' or 'Business'.)
        """
        def set_EntityType(self, value):
            InputSet._set_input(self, 'EntityType', value)

        """
        Set the value of the LoginEmail input for this choreography. ((string) The login email for the new account)
        """
        def set_LoginEmail(self, value):
            InputSet._set_input(self, 'LoginEmail', value)

        """
        Set the value of the Password input for this choreography. ((string) The developer's password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)


"""
A ResultSet with methods tailored to the values returned by the CreateAccount choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateAccountResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google AdSense.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateAccountChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateAccountResultSet(response, path)
