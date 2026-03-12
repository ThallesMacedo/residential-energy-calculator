import streamlit as st
import storage
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="HomeWatt",
    page_icon="⚡",
    layout="wide"
)

# -------- LOAD DATA --------

appliances = storage.load_data()

# -------- HEADER --------

col1, col2 = st.columns([1,3])

with col1:
    st.image("logo.png", width=150)

with col2:
    st.title("HomeWatt")
    st.caption("Residential Energy Consumption Calculator")

st.divider()

# -------- MENU --------

menu = st.sidebar.radio(
    "Menu",
    ["🏠 Home", "➕ Add Appliance", "📋 Appliances"]
)

# -------- HOME --------

if menu == "🏠 Home":

    st.subheader("Energy Dashboard")

    if not appliances:
        st.info("No appliances registered yet.")
    else:

        names = [a["appliance_name"] for a in appliances]
        consumptions = [a["monthly_consumption"] for a in appliances]
        costs = [a["monthly_cost"] for a in appliances]

        total_consumption = sum(consumptions)
        total_cost = sum(costs)

        avg_consumption = total_consumption / len(appliances)

        highest_consumption = max(appliances, key=lambda a: a["monthly_consumption"])
        highest_cost = max(appliances, key=lambda a: a["monthly_cost"])

        # METRIC CARDS
        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Consumption",
            f"{total_consumption:.2f} kWh"
        )

        col2.metric(
            "Total Energy Cost",
            f"R$ {total_cost:.2f}"
        )

        col3.metric(
            "Average Consumption",
            f"{avg_consumption:.2f} kWh"
        )

        st.divider()

        # MAIN GRAPH
        st.subheader("Consumption by Appliance")

        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        ax.bar(names, consumptions)
        ax.set_xlabel("Appliances")
        ax.set_ylabel("kWh")
        ax.set_title("Monthly Energy Consumption")
        plt.xticks(rotation=45)

        st.pyplot(fig)

        st.divider()

        # PIE + RANKING

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Energy Distribution")

            fig2, ax2 = plt.subplots()
            ax2.pie(consumptions, labels=names, autopct="%1.1f%%")
            ax2.set_title("Consumption Share")

            st.pyplot(fig2)

        with col2:

            st.subheader("Top Energy Consumers")

            ranking = sorted(
                appliances,
                key=lambda a: a["monthly_consumption"],
                reverse=True
            )

            for i, appliance in enumerate(ranking, start=1):

                st.write(
                    f"{i}. **{appliance['appliance_name']}** — "
                    f"{appliance['monthly_consumption']:.2f} kWh"
                )

        st.divider()

        # HIGHLIGHT CARDS

        col1, col2 = st.columns(2)

        col1.success(
            f"⚡ Highest Consumption Appliance: "
            f"{highest_consumption['appliance_name']}"
        )

        col2.warning(
            f"💰 Highest Cost Appliance: "
            f"{highest_cost['appliance_name']}"
        )
# -------- ADD APPLIANCE --------

elif menu == "➕ Add Appliance":

    st.subheader("Add Appliance")

    name = st.text_input("Appliance name")
    power = st.number_input("Power (Watts)", min_value=0.0)
    hours = st.number_input("Hours per day", min_value=0)
    days = st.number_input("Days per month", min_value=0)
    price = st.number_input("Price per kWh (R$)", min_value=0.0)

    if st.button("Add Appliance"):

        daily = (power / 1000) * hours
        monthly = daily * days
        cost = monthly * price

        appliances.append({
            "appliance_name": name,
            "monthly_consumption": monthly,
            "monthly_cost": cost
        })

        storage.save_data(appliances)

        st.success("Appliance added successfully!")

# -------- LIST APPLIANCES --------

elif menu == "📋 Appliances":

    st.subheader("Manage Appliances")

    if not appliances:
        st.info("No appliances registered.")
    else:

        for i, appliance in enumerate(appliances):

            with st.expander(f"{appliance['appliance_name']}"):

                st.write(f"Consumption: {appliance['monthly_consumption']:.2f} kWh")
                st.write(f"Cost: R$ {appliance['monthly_cost']:.2f}")

                col1, col2 = st.columns(2)

                # -------- REMOVE --------

                if col1.button(f"Remove {i}"):

                    appliances.pop(i)
                    storage.save_data(appliances)

                    st.success("Appliance removed")
                    st.rerun()

                # -------- EDIT --------

                if col2.button(f"Edit {i}"):

                    st.session_state["edit_index"] = i

        # -------- EDIT FORM --------

        if "edit_index" in st.session_state:

            idx = st.session_state["edit_index"]
            appliance = appliances[idx]

            st.divider()
            st.subheader("Edit Appliance")

            new_name = st.text_input(
                "Name",
                value=appliance["appliance_name"]
            )

            new_power = st.number_input("Power (Watts)", min_value=0.0)
            new_hours = st.number_input("Hours per day", min_value=0)
            new_days = st.number_input("Days per month", min_value=0)
            new_price = st.number_input("Price per kWh", min_value=0.0)

            if st.button("Update Appliance"):

                daily = (new_power / 1000) * new_hours
                monthly = daily * new_days
                cost = monthly * new_price

                appliances[idx] = {
                    "appliance_name": new_name,
                    "monthly_consumption": monthly,
                    "monthly_cost": cost
                }

                storage.save_data(appliances)

                del st.session_state["edit_index"]

                st.success("Appliance updated successfully!")
                st.rerun()