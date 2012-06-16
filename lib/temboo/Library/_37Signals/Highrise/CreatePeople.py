
###############################################################################
#
# CreatePeople
# Creates a new contact record in your Highrise CRM.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreatePeople(Choreography):

    """
    Create a new instance of the CreatePeople Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Highrise/CreatePeople')


    def new_input_set(self):
        return CreatePeopleInputSet()

    def _make_result_set(self, result, path):
        return CreatePeopleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreatePeopleChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreatePeople
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreatePeopleInputSet(InputSet):
        """
        Set the value of the AccountName input for this choreography. ((string) The Highrise account name for you or your company. This is the first part of your account URL.)
        """
        def set_AccountName(self, value):
            InputSet._set_input(self, 'AccountName', value)

        """
        Set the value of the Background input for this choreography. ((optional, string) Corresponds to the background field in Highrise)
        """
        def set_Background(self, value):
            InputSet._set_input(self, 'Background', value)

        """
        Set the value of the CompanyName input for this choreography. ((optional, string) Corresponds to the company name field in Highrise.)
        """
        def set_CompanyName(self, value):
            InputSet._set_input(self, 'CompanyName', value)

        """
        Set the value of the EmailAddress input for this choreography. ((optional, string) Corresponds to the email address field in Highrise.)
        """
        def set_EmailAddress(self, value):
            InputSet._set_input(self, 'EmailAddress', value)

        """
        Set the value of the FirstName input for this choreography. ((string) Corresponds to the first name field in Highrise.)
        """
        def set_FirstName(self, value):
            InputSet._set_input(self, 'FirstName', value)

        """
        Set the value of the HomePhone input for this choreography. ((optional, string) Corresponds to the home phone field in Highrise.)
        """
        def set_HomePhone(self, value):
            InputSet._set_input(self, 'HomePhone', value)

        """
        Set the value of the LastName input for this choreography. ((optional, string) Corresponds to the last name field in Highrise.)
        """
        def set_LastName(self, value):
            InputSet._set_input(self, 'LastName', value)

        """
        Set the value of the Password input for this choreography. ((string) Your Highrise password. You can also use the value 'X' as a dummy password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Title input for this choreography. ((optional, string) Corresponds to the title field in Highrise.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Username input for this choreography. ((string) Your Highrise API key.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the WorkPhone input for this choreography. ((optional, string) Corresponds to the work phone field in Highrise.)
        """
        def set_WorkPhone(self, value):
            InputSet._set_input(self, 'WorkPhone', value)


"""
A ResultSet with methods tailored to the values returned by the CreatePeople choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreatePeopleResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Highrise.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreatePeopleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreatePeopleResultSet(response, path)
