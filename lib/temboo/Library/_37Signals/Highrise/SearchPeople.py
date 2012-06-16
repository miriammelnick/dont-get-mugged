
###############################################################################
#
# SearchPeople
# Lets you search your Highrise CRM by specifying an email search criteria.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchPeople(Choreography):

    """
    Create a new instance of the SearchPeople Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Highrise/SearchPeople')


    def new_input_set(self):
        return SearchPeopleInputSet()

    def _make_result_set(self, result, path):
        return SearchPeopleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchPeopleChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchPeople
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchPeopleInputSet(InputSet):
        """
        Set the value of the AccountName input for this choreography. ((string) The Highrise account name for you or your company. This is the first part of your account URL.)
        """
        def set_AccountName(self, value):
            InputSet._set_input(self, 'AccountName', value)

        """
        Set the value of the City input for this choreography. ((optional, string) Allows you to search by the city field in Highrise.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the Country input for this choreography. ((optional, string) Allows you to search by the country field in Highrise.)
        """
        def set_Country(self, value):
            InputSet._set_input(self, 'Country', value)

        """
        Set the value of the EmailAddress input for this choreography. ((optional, string) Allows you to search by the email address field in Highrise.)
        """
        def set_EmailAddress(self, value):
            InputSet._set_input(self, 'EmailAddress', value)

        """
        Set the value of the Password input for this choreography. ((string) Your Highrise password. You can also use the value 'X' as a dummy password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Phone input for this choreography. ((optional, string) Allows you to search by the phone field in Highrise.)
        """
        def set_Phone(self, value):
            InputSet._set_input(self, 'Phone', value)

        """
        Set the value of the State input for this choreography. ((optional, string) Allows you to search by the state field in Highrise.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Username input for this choreography. ((string) Your Highrise API Key.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the Zip input for this choreography. ((optional, string) Allows you to search by the ZIP field in Highrise.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the SearchPeople choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchPeopleResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Highrise.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchPeopleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchPeopleResultSet(response, path)
